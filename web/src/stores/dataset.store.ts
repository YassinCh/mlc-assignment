import { defineStore } from "pinia";
import { ref } from "vue";
import { AxiosError } from "axios";
import api from "@/api";
import { Dataset } from "@/interfaces/dataset.interface";

export const useDatasetStore = defineStore("datasets", () => {
    const datasets = ref(undefined as Array<Dataset> | undefined);

    async function fetchDatasets(): Promise<void> {
        try {
            const response = await api.get(`/datasets`);
            datasets.value = response.data as Array<Dataset>;
        } catch (error: AxiosError) {
            console.error(error);
            datasets.value = undefined;
        }
    }

    async function deleteDataset(id: string): Promise<void> {
        try {
            const response = await api.delete(`/datasets/${id}`);
            if (response.status !== 204) {
                throw new Error("Failed to delete dataset");
            }
            if (datasets.value) {
                datasets.value = datasets.value.filter((d: Dataset) => d.id !== id)
            }
        } catch (error: AxiosError) {
            console.error(error);
        }
    }

    async function uploadDataset(name: string, file: File): Promise<Dataset | undefined> {
        try {
            const data = new FormData();
            data.append("dataset_name", name);
            data.append("excel_file", file);
            const response = await api.post(`/dataset_parsers/excel`, data, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });
            const dataset = response.data as Dataset;
            datasets.value?.push(dataset);
            return dataset;
        } catch (error: AxiosError) {
            console.error(error);
        }

        return undefined;
    }

    return {
        datasets,
        fetchDatasets,
        deleteDataset,
        uploadDataset,
    }
});
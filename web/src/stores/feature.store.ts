import { defineStore } from "pinia";
import { Feature } from "@/interfaces/dataset.interface";
import { createBaseStore } from "./base.store";

export const useFeatureStore = defineStore("features", () => {
    const { items: features, fetchItems } = createBaseStore<Feature>("/dataset_features");

    async function fetchFeatures(datasetId: string): Promise<void> {
        await fetchItems({ dataset_id: datasetId });
    }

    return {
        features,
        fetchFeatures,
    };
});
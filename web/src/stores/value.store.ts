import { defineStore } from "pinia";
import { Value } from "@/interfaces/dataset.interface";
import { createBaseStore } from "./base.store";

export const useValueStore = defineStore("datasetValues", () => {
    const { items: values, fetchItems } = createBaseStore<Value>("/dataset_values");

    async function fetchValues(params: { product_id?: string; feature_id?: string } = {}): Promise<void> {
        await fetchItems(params);
    }

    return {
        values,
        fetchValues,
    };
});
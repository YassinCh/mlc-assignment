import { defineStore } from "pinia";
import { Product } from "@/interfaces/dataset.interface";
import { createBaseStore } from "./base.store";

export const useProductStore = defineStore("Products", () => {
    const { items: products, fetchItems } = createBaseStore<Product>("/dataset_products");

    async function fetchProducts(Id: string): Promise<void> {
        await fetchItems({ _id: Id });
    }

    return {
        products,
        fetchProducts,
    };
});
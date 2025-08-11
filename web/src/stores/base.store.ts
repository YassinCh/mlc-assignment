import { ref, Ref } from "vue";
import { AxiosError } from "axios";
import api from "@/api";

export function createBaseStore<T>(endpoint: string) {
    const items: Ref<Array<T> | undefined> = ref(undefined);

    async function fetchItems(params: Record<string, any> = {}): Promise<void> {
        try {
            const queryParams = new URLSearchParams();
            Object.entries(params).forEach(([key, value]) => {
                if (value !== undefined && value !== null) {
                    queryParams.append(key, value.toString());
                }
            });

            const url = queryParams.toString()
                ? `${endpoint}?${queryParams.toString()}`
                : endpoint;

            const response = await api.get(url);
            items.value = response.data as Array<T>;
        } catch (error: AxiosError) {
            console.error(error);
            items.value = undefined;
        }
    }

    return {
        items,
        fetchItems,
    };
}
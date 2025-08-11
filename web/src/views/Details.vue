<template>
    <v-btn class="mb-4" :to="'/'">
        <v-icon>mdi-arrow-left</v-icon>
        Back
    </v-btn>
    <h2>
        {{ selectedDataset?.name }}
    </h2>
    <v-card class="pa-2">
        <v-data-table
            :items="tableData"
            :headers="tableHeaders"
            no-data-text="No data found for this dataset."
            class="dataset-table"
        >
        </v-data-table>
    </v-card>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { useRoute } from 'vue-router'
import { useDatasetStore } from '@/stores/dataset.store';
import { useFeatureStore } from '@/stores/feature.store';
import { useProductStore } from '@/stores/product.store';
import { useValueStore } from '@/stores/value.store';
import { type Dataset, type Feature, type Product, type Value } from "@/interfaces/dataset.interface";

const datasetStore = useDatasetStore();
const featureStore = useFeatureStore();
const productStore = useProductStore();
const valueStore = useValueStore();
const route = useRoute()
const datasetId = route.params.datasetId as string;

const tableData = ref<any[]>([]);

const selectedDataset = computed(() => {
    return datasetStore.datasets?.find((dataset: Dataset) => dataset.id === datasetId as string);
});

const buildTableData = () => {
    const features = featureStore.features || [];
    const products = productStore.products || [];
    const values = valueStore.values || [];

    const data = products.map(product => {
        const row: any = {
            product_id: product.id,
            product: `Product ${products.indexOf(product) + 1}`
        };
        
        features.forEach(feature => {
            const value = values.find(v => 
                v.product_id === product.id && v.feature_id === feature.id
            );
            row[feature.id] = value?.value || '-';
        });
        
        return row;
    });
    
    tableData.value = data;
};

const tableHeaders = computed(() => {
    const features = featureStore.features || [];
    return [
        { title: 'Product', key: 'product' },
        ...features.map(feature => ({
            title: feature.name,
            key: feature.id
        }))
    ];
});

onMounted(async () => {
    await datasetStore.fetchDatasets();
    await Promise.all([
        featureStore.fetchFeatures(datasetId),
        productStore.fetchProducts(datasetId),
        valueStore.fetchValues()
    ]);
    buildTableData();
});
</script>
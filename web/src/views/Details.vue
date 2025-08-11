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
            no-data-text="Dit component is nog niet geïmplementeerd. Probeer het project uit te breiden zodat je hier de data kan inzien van je dataset."
        >
        </v-data-table>
    </v-card>
</template>

<script setup lang="ts">
import { computed, onMounted } from "vue";
import { useRoute } from 'vue-router'
import { useDatasetStore } from '@/stores/dataset.store';
import { type Dataset } from "@/interfaces/dataset.interface";

// TODO: Laad de dataset data in via een store en laat deze zien in de v-data-table. Er zijn nog geen stores aangemaakt 
//       voor dataset features, products en values, dus je moet deze zelf aanmaken.
// Hints:
// - Kijk naar de Vuetify documentatie voor v-data-table: Kijk naar de documentatie van Vuetify (https://vuetifyjs.com/en/components/data-tables/basics/#usage)
// - Kijk naar de documentatie van Pinia (https://pinia.vuejs.org/core-concepts/) 

const datasetStore = useDatasetStore();
const route = useRoute()
const datasetId = parseInt(route.params.datasetId);

const selectedDataset = computed(() => {
    return datasetStore.datasets?.find((dataset: Dataset) => dataset.id === datasetId as number);
});

onMounted(async () => await datasetStore.fetchDatasets());
</script>
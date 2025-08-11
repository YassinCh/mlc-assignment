<template>
    <h2>Datasets</h2>
    <v-card class="pa-2">
        <DatasetCreateDialog />
        <v-data-table :items="datasets" :headers="headers"
            no-data-text="No datasets found. Click the button above to create one.">
            <template #item.created_at="{ value }">
                {{ (new Date(value)).toLocaleString() }}
            </template>
            <template #item.actions="{ item }">
                <v-tooltip text="Details" location="top">
                    <template #activator="{ props }">
                        <v-btn v-bind="props" color="primary" variant="text" density="comfortable" icon="mdi-magnify"
                            :to="{ name: 'details', params: { datasetId: item.id } }"></v-btn>
                    </template>
                </v-tooltip>
                <v-tooltip text="Delete" location="top">
                    <template #activator="{ props }">
                        <v-btn v-bind="props" color="error" variant="text" density="comfortable" icon="mdi-delete"
                            @click="deleteDataset(item)"></v-btn>
                    </template>
                </v-tooltip>
            </template>
        </v-data-table>
    </v-card>
</template>

<script setup lang="ts">
import { computed, ref, onMounted } from "vue";
import DatasetCreateDialog from "@/components/DatasetCreateDialog.vue";
import { useDatasetStore } from '@/stores/dataset.store';

const datasetStore = useDatasetStore();
const headers = ref([
    { title: "ID", value: "id" },
    { title: "Name", value: "name" },
    { title: "Created", value: "created_at" },
    { title: "Actions", value: "actions", width: "220px", sortable: false },
]);

const datasets = computed(() => {
    return datasetStore.datasets;
});

async function deleteDataset(dataset: { id: number }) {
    await datasetStore.deleteDataset(dataset.id);
}

onMounted(async () => await datasetStore.fetchDatasets());

</script>
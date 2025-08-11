<template>
    <v-dialog v-model="open" max-width="800">
        <template #activator="{ props }">
            <slot name="activator" :props="props">
                <v-btn v-bind="props" color="success" prepend-icon="mdi-upload" text="Upload" variant="elevated"
                    class="ma-2"></v-btn>
            </slot>
        </template>

        <v-card>
            <v-toolbar title="Upload" color="primary">
                <v-spacer></v-spacer>
                <v-btn icon="mdi-close" variant="text" @click="open = false"></v-btn>
            </v-toolbar>

            <v-card-text>
                <v-form ref="form" v-model="valid" @submit.prevent>
                    <v-text-field v-model="datasetName" prepend-icon="mdi-file-document-edit-outline"
                        label="Dataset name" required></v-text-field>
                    <v-file-input v-model="datasetFiles"
                        accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" label="Dataset file"
                        required></v-file-input>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn :loading="loading" :disabled="!valid" variant="flat" color="success" @click="submit">
                            Upload
                        </v-btn>
                    </v-card-actions>
                    <p v-if="!valid">{{ alertError }}</p>
                </v-form>
            </v-card-text>
        </v-card>
    </v-dialog>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { useDatasetStore } from '@/stores/dataset.store';

const datasetStore = useDatasetStore();

const open = ref(false);
const datasetName = ref("");
const datasetFiles = ref([] as File[]);
const loading = ref(false);
const alertError = ref(undefined as string | undefined);
const valid = ref(false);

async function submit() {
    alertError.value = undefined;
    loading.value = true;
    const result = await datasetStore.uploadDataset(datasetName.value, datasetFiles.value[0])
    if (!result) {
        alertError.value = "Failed to upload dataset";
    }
    else {
        open.value = false;
    }
    loading.value = false;
}

watch(open, () => {
    datasetName.value = "";
    datasetFiles.value = [];
});
</script>
<template>
	<v-layout ref="app">
		<v-app-bar color="primary" title="MLC Developer Assessment"></v-app-bar>

		<v-main>
			<v-container>
				<router-view />
			</v-container>
		</v-main>

		<v-footer app color="footer">
			<v-spacer></v-spacer>
			<span class="text-caption">© Squadra - Machine Learning Company</span>
		</v-footer>
	</v-layout>
</template>

<script lang="ts" setup>
import { RouterView } from 'vue-router';

</script>
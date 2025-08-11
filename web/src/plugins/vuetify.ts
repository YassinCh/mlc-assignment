import 'vuetify/styles';
import "@mdi/font/css/materialdesignicons.css";
import { createVuetify, type ThemeDefinition } from 'vuetify';
import { aliases, mdi } from 'vuetify/iconsets/mdi';

const light: ThemeDefinition = {
	dark: false,
	colors: {
		background: '#F9F9F9',
		primary: '#168BB4',
		footer: '#023346',
		accent: '#E37903'
	},
}

const dark: ThemeDefinition = {
	dark: true,
	colors: {
		primary: '#f78b33',
		footer: '#191919',
		accent: '#E37903'
	},
}

const vuetify = createVuetify({
	theme: {
		defaultTheme: 'light',
		variations: {
			colors: ['primary', 'accent', 'surface'],
			lighten: 5,
			darken: 4
		},
		themes: {
			light,
			dark
		}
	},
	icons: {
		defaultSet: 'mdi',
		aliases,
		sets: {
			mdi,
		}
	}
})

export default vuetify;

function initializeTheme() {
	// Load theme from local storage
	const theme = localStorage.getItem('theme')
	if (theme) vuetify.theme.global.name.value = theme;
	else vuetify.theme.global.name.value = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';

	// Change theme if no theme is set when browser color scheme preference changes
	window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
		vuetify.theme.global.name.value = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
		localStorage.removeItem('theme');
	})
}

initializeTheme();
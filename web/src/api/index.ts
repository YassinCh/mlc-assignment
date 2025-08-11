// import Vue from "vue";
import axios from "axios";

export const baseURL = `${import.meta.env.VITE_BACKEND_DOMAIN}/api`;

const api = axios.create({
	baseURL: baseURL
});

export default api;

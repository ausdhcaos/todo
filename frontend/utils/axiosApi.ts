import axios from "axios";
import { cookies } from "next/headers";
import { is_authenticated } from "./auth";

const headers: any = {};

export const axiosApi = axios.create({
  baseURL: process.env.NEXT_PUBLIC_BACKEND_HOST,
  headers,
});

axiosApi.interceptors.request.use((config) => {
  if (is_authenticated()) {
    config.headers["Authorization"] = `Bearer ${
      cookies().get("access_token")?.value
    }`;
  }
  return config;
});

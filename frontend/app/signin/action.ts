"use server";

import { redirect } from "next/navigation";
import { cookies } from "next/headers";
import { axiosApi } from "@/utils/axiosApi";

export async function signin(email: string, password: string) {
  const params = new URLSearchParams();
  params.append("username", email);
  params.append("password", password);
  params.append("grant_type", "password");

  const res = await axiosApi.post("/users/token", params);

  cookies().set("access_token", res.data.access_token, {
    expires: new Date(res.data.exp),
  });

  redirect("/todos");
}

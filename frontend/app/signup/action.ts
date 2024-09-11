"use server";

import { redirect } from "next/navigation";
import { axiosApi } from "@/utils/axiosApi";

export async function createUser(email: string, password: string) {
  await axiosApi.post("/users/signup", null, {
    params: {
      email_address: email,
      password: password,
    },
  });

  redirect("/signin");
}

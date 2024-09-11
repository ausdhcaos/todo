"use server";

import { axiosApi } from "@/utils/axiosApi";
import { revalidatePath } from "next/cache";

export async function createTodo(description: string) {
  await axiosApi.post("/todos", null, {
    params: { description },
  });

  revalidatePath("/todos");
}

export async function deleteTodo(id: number) {
  await axiosApi.delete(`/todos/${id}`);

  revalidatePath("/todos");
}

export async function updateTodo(id: number, status: string) {
  await axiosApi.put(`todos/${id}`, null, {
    params: {status},
  });
}
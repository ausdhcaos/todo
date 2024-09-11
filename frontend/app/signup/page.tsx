import { is_authenticated } from "@/utils/auth";
import Form from "./form";
import { redirect } from "next/navigation";

export default function Signup() {
  if (is_authenticated()) {
    redirect("/todos");
  }

  return <Form />;
}

import { is_authenticated } from "@/utils/auth";
import Form from "./form";
import { redirect } from "next/navigation";

export default function Signin() {
  if (is_authenticated()) {
    redirect("/todos");
  }

  return <Form />;
}

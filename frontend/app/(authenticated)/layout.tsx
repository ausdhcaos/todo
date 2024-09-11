import { is_authenticated } from "@/utils/auth";
import { redirect } from "next/navigation";
import Nav from "./nav";

export default function AuthenticatedLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  if (!is_authenticated()) {
    redirect("/signin");
  }

  return (
    <div>
      <Nav />
      {children}
    </div>
  );
}

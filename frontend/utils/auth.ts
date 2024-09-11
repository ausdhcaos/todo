import { cookies } from "next/headers";

export const is_authenticated = () => {
  const access_token = cookies().get("access_token")?.value;

  if (!access_token) {
    return false;
  }

  return true;
};

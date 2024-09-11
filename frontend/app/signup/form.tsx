"use client";

import { useState } from "react";
import { createUser } from "./action";
import Link from "next/link";

export default function Form() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  return (
    <div className="p-2">
      <h1>Signup</h1>
      <br />

      <label>Email address</label>
      <br />
      <input
        className="p-1 border-black border"
        value={email}
        onChange={(event) => setEmail(event.target.value)}
      />
      <br />
      <label>Password</label>
      <br />
      <input
        className="p-1 border-black border"
        type="password"
        value={password}
        onChange={(event) => setPassword(event.target.value)}
      />
      <br />
      <label>Confirm password</label>
      <br />
      <input
        className="p-1 border-black border"
        type="password"
        value={confirmPassword}
        onChange={(event) => setConfirmPassword(event.target.value)}
      />

      <br />
      <br />
      <button
        className="p-1 border-black border mb-4"
        onClick={async () => {
          if (email === "" || password === "" || confirmPassword === "") {
            alert("Please fill all the fields");
            return;
          }

          if (password !== confirmPassword) {
            alert("Password does not match");
            return;
          }

          await createUser(email, password);
        }}
      >
        Sign up
      </button>

      <br />
      <Link href="/signin" passHref className="text-blue-950">
        Go to Sign in
      </Link>
    </div>
  );
}

"use client";

import { useState } from "react";
import { signin } from "./action";
import Link from "next/link";

export default function Form() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  return (
    <div className="p-2">
      <h1>Signin</h1>
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
      <br />
      <button
        className="p-1 border-black border mb-4"
        onClick={async () => {
          if (email === "" || password === "") {
            alert("Please fill all the fields");
            return;
          }

          await signin(email, password);
        }}
      >
        Sign in
      </button>

      <br />
      <Link href="/signup" passHref className="text-blue-950">
        Go to Sign up
      </Link>
    </div>
  );
}

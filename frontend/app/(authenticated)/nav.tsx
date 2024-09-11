"use client";

import { signout } from "./action";

export default function Nav() {
  return (
    <div className="mb-4">
      <button
        className="p-1 border-black border"
        onClick={() => {
          signout();
        }}
      >
        sign out
      </button>
    </div>
  );
}

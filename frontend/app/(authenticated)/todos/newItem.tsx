"use client";

import { useState } from "react";
import { createTodo } from "./action";

export default function NewItem() {
  const [description, setDescription] = useState("");

  return (
    <div className="mt-4">
      <input
        className="p-1 border-black border mr-2"
        value={description}
        onChange={(event) => setDescription(event.target.value)}
      />
      <button
        className="p-1 border-black border"
        onClick={async () => {
          if (!description) {
            alert("Description is required");
            return;
          }

          await createTodo(description);

          setDescription("");
        }}
      >
        Add new
      </button>
    </div>
  );
}

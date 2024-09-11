"use client";

import { useEffect, useState } from "react";
import { deleteTodo, updateTodo } from "./action";

export default function Item({
  description,
  id,
  status
}: {
  description: string;
  id: number;
  status: string;
}) {
  const [statusChecked, setStatusChecked] = useState(false);

  useEffect(()=>{
    setStatusChecked(status === "completed");
  }, [])

  return (
    <div className="mb-2">
      <input 
        type="checkbox"
        checked={statusChecked}
        onChange={async (event) =>{
           setStatusChecked(event.target.checked);
           await updateTodo(id, event.target.checked ? "completed" : "pending");
          }}
      />
      {description}{" "}
      {status}
      <button
        className="p-1 border-black border"
        onClick={async () => {
          await deleteTodo(id);
        }}
      >
        delete
      </button>
    </div>
  );
  



}



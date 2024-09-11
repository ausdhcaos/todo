import { axiosApi } from "@/utils/axiosApi";
import Item from "./item";
import NewItem from "./newItem";

export default async function Todos() {
  const res = await axiosApi.get("/todos");

  return (
    <div>
      {res.data.map((x: any) => (
        <Item key={x.id} description={x.description} id={x.id} status={x.status} />
      ))}
      <NewItem />
    </div>
  );
}

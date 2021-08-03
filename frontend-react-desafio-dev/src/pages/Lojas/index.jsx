import { ListLojas } from "../../components/ListLojas";

export const Lojas = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Lojas</h1>
      <p style={{ textAlign: "center" }}>
        Clique em cada loja para ver os detalhes da transação
      </p>
      <ListLojas />
    </>
  );
};

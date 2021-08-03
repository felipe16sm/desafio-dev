import { useParams } from "react-router-dom";
import { CardLojaTransacoes } from "../../components/CardLojaTransacoes";

export const LojaTransacoes = () => {
  let { idLoja } = useParams();

  return (
    <>
      <CardLojaTransacoes idLoja={idLoja} />
    </>
  );
};

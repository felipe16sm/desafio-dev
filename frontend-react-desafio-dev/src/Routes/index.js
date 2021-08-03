import { Switch, Route } from "react-router-dom";
import { Home } from "../pages/Home";
import { LojaTransacoes } from "../pages/LojaTransacoes";
import { Lojas } from "../pages/Lojas";

export const Routes = () => {
  return (
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/loja-transacoes/:idLoja" component={LojaTransacoes} />
      <Route exact path="/lojas" component={Lojas} />
    </Switch>
  );
};

import { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";
import { api } from "../../api";
import { CardLoja } from "../CardLoja";

export const ListLojas = () => {
  const history = useHistory();
  const [listLojasData, setlistLojasData] = useState([]);

  useEffect(() => {
    api
      .get("stores/")
      .then((response) => {
        console.log(response.data);
        setlistLojasData(response.data);
      })
      .catch((error) => {
        console.log(error.response);
      });
  }, []);

  return (
    <div>
      {listLojasData.map((lojaData, index) => {
        return <CardLoja lojaData={lojaData} key={index} />;
      })}
    </div>
  );
};

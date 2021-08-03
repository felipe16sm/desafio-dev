import React from "react";
import {
  AppBar,
  Toolbar,
  makeStyles,
  Typography,
  Button,
} from "@material-ui/core";

import { useHistory } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  button: {
    marginRight: "10px",
  },
  title: {
    flexGrow: 1,
  },
}));

export const NavBar = () => {
  const history = useHistory();
  const classes = useStyles();

  const handleButtonHome = () => {
    history.push("/");
  };

  const handleButtonLojas = () => {
    history.push("/lojas");
  };

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Desafio-dev-Fronted
          </Typography>
          <Button
            onClick={handleButtonHome}
            variant="outlined"
            color="inherit"
            className={classes.button}
          >
            Home
          </Button>
          <Button
            onClick={handleButtonLojas}
            variant="outlined"
            color="inherit"
          >
            Lojas
          </Button>
        </Toolbar>
      </AppBar>
    </div>
  );
};

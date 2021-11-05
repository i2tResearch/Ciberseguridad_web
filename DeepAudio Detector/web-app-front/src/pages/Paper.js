import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';

const useStyles = makeStyles((theme) => ({
    root: {
      backgroundColor: "#121212",
      textAlign: "center",
      fontFamily: "Roboto",
      fontStyle: "light",
      color: "white",
    },
}));

function Home() {
    const classes = useStyles();
    return (
        <div className={classes.root}>
            <Typography style={{padding: "3%"}} variant="h1">DeepDetector</Typography>
            <Grid style={{paddingBottom: "5%", width: "100%"}} container spacing={3}>
                <Grid item xs>
                    <Typography variant="h4">Cristhian Castillo</Typography>
                </Grid>
                <Grid item xs>
                    <Typography variant="h4">Kevin Zarama</Typography>
                </Grid>
                <Grid item xs>
                    <Typography variant="h4">Cristian Urcuqui</Typography>
                </Grid>
            </Grid>
            <Typography style={{paddingBottom: "3%"}} variant="h4">University ICESI<br/>2021</Typography>
            <Grid style={{paddingBottom: "5%", width: "100%"}} container spacing={2}>
                <Grid item xs>
                    <Typography variant="h4">Paper</Typography>
                </Grid>
                <Grid item xs>
                    <Typography variant="h4">github</Typography>
                </Grid>
            </Grid>
			<hr style={{width: "75%"}}/>
            <div style={{textAlign: "center"}}>
                <Typography style={{padding: "3%"}} variant="h3">Abstract</Typography>
                <Typography style={{paddingBottom: "3%", width: "75%", margin: 0}} variant="subtitle1">loremLorem ipsum dolor sit amet consectetur adipiscing elit justo placerat, sem leo montes condimentum potenti cursus lectus dictum vivamus fringilla, nascetur tellus iaculis ridiculus per interdum facilisis odio. Faucibus quisque praesent convallis vivamus aliquet, parturient metus ullamcorper imperdiet enim, platea hendrerit augue commodo. Eget malesuada orci commodo quam tempus sapien magna rhoncus, nulla bibendum vitae dapibus ut consequat vestibulum litora purus, odio in scelerisque nostra habitasse donec curabitur.</Typography>
            </div>
        </div>
    )
}

export default Home;

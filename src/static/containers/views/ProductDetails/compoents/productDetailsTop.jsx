import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
import { Link } from "react-router-dom";

import GridContainer from "../../../../components/Grid/GridContainer.jsx";
import GridItem from "../../../../components/Grid/GridItem.jsx";
import Parallax from "../../../../components/Parallax/Parallax.jsx";
import Button from "../../../../components/CustomButtons/Button.jsx";
import styles from "../../../../../assets/jss/material-kit-pro-react/views/ecommerceSections/latestOffersStyle.jsx";

const SectionLatestOffers = props => {
    const { classes } = props;
    const img = props.coursesInfoData.image
    return (

        <div className={classes.section}>
            <Parallax
                image={props.coursesInfoData.image}
                className={classes.parallax90}
            >
                <div className={classes.container} style={{top:"-100px"}}>
                    <GridContainer>
                        <GridItem>
                            <div className={classes.brand}>
                                <h2 className={classes.textWhite}>
                                    {props.coursesInfoData.name}
                                </h2>
                                {console.log(props.coursesInfoData)}
                                <br/>
                                <span>{props.coursesInfoData.desc}</span>
                                <hr/>
                                <span>
                                    难度 初级 · 
                                    时长{props.coursesInfoData.learn_times}小时 · 
                                    学习人数{props.coursesInfoData.students} · 人
                                    收藏人数 {props.coursesInfoData.fav_nums} . 人
                                </span>
                                <br className={classes.width70} />
                                <div  className={classes.title}>
                                    <div style={{fontSize:"35px"}}>￥ {props.coursesInfoData.shop_price} </div>
                                    <Button round color="rose">
                                        <Link to="/ShoppingCart" style={{color:"white"}}>
                                          加入购物车                                        
                                        </Link>
                                    </Button>
                                </div>
                            </div>
                        </GridItem>
                    </GridContainer>
                </div>
            </Parallax>
        </div>
    );
};

export default withStyles(styles)(SectionLatestOffers);

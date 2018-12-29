import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
import ChatBubble from "@material-ui/icons/ChatBubble";
import Favorite from "@material-ui/icons/Favorite";
import { Link } from "react-router-dom";


import GridItem from "../../../../components/Grid/GridItem";
import Card from "../../../../components/Card/Card";
import CardHeader from "../../../../components/Card/CardHeader";
import CardBody from "../../../../components/Card/CardBody.jsx";
import GridContainer from "../../../../components/Grid/GridContainer.jsx";
import CardFooter from "../../../../components/Card/CardFooter.jsx";
import office1 from "../../../../../assets/img/examples/office1.jpg";
import styles from "../../../../../assets/jss/material-kit-pro-react/views/componentsSections/sectionCards.jsx";
import Badge from "../../../../components/Badge/Badge.jsx";

import christian from "../../../../../assets/img/faces/christian.jpg";

class SingleItem extends React.Component {

    render() {
        const { classes } = this.props;
        return (
            <GridContainer>
                {
                    this.props.resultsData.map(item => {
                        return(
                            <GridItem xs={12} sm={6} md={4} lg={4}>
                                <Card>
                                    <CardHeader image>
                                        <Link to={'/ProductDetails/'+item.id}>
                                            <img src={item.image} alt="..." />
                                            <div className={classes.cardTitleAbsolute}>
                                                {item.name}
                                            </div>
                                        </Link>
                                        <div
                                            className={classes.coloredShadow}
                                            style={{
                                                backgroundImage: `url(${item.image})`,
                                                opacity: "1"
                                            }}
                                        />
                                    </CardHeader>
                                    <CardBody>
                                        <Badge color="rose" className={classes.margin15}>VIP</Badge>
                                        <Badge color="#1E90FF" className={classes.margin15}>pyton</Badge>
                                        <Badge color="primary" className={classes.margin15}>硬件+软件</Badge>
                                        <Badge color="warning" className={classes.margin15}>推荐入门</Badge>
                                        <div className={classes.cardDescription}>
                                            {item.desc}
                                        </div>
                                    </CardBody>
                                    <CardFooter>
                                        <div className={classes.author}>
                                            <a href="#pablo" onClick={e => e.preventDefault()}>
                                                <img
                                                    src={christian}
                                                    alt="..."
                                                    className={`${classes.imgRaised} ${
                                                        classes.avatar
                                                        }`}
                                                />
                                                <span className={classes.positionAbsBottom1_5em}>Lord Alex</span>
                                            </a>
                                        </div>
                                        <div className={`${classes.stats} ${classes.mlAuto}`}>
                                            <Favorite />
                                            <span className={classes.marginTop6}>{item.fav_nums}</span>
                                            <ChatBubble />
                                            <span className={classes.marginTop6}> {item.students}</span>
                                        </div>
                                    </CardFooter>
                                </Card>

                            </GridItem>
                        )
                    })
                }
            </GridContainer>
                
        )
    }
}

export default withStyles(styles)(SingleItem)
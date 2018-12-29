import React from "react";

// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// core components
import GridContainer from "../../../../components/Grid/GridContainer.jsx";
import GridItem from "../../../../components/Grid/GridItem.jsx";
import Card from "../../../../components/Card/Card.jsx";
import CardHeader from "../../../../components/Card/CardHeader.jsx";
import CardBody from "../../../../components/Card/CardBody.jsx";
import Warning from "../../../../components/Typography/Warning.jsx";
import Button from "../../../../components/CustomButtons/Button.jsx";

import styles from "../../../../../assets/jss/material-kit-pro-react/views/componentsSections/sectionCards.jsx";


import color1 from "../../../../../assets/img/examples/color1.jpg";


class SectionCards extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      activeRotate1: "",
      activeRotate2: ""
    };
  }
  componentDidMount() {
    const { classes } = this.props;
    var rotatingCards = document.getElementsByClassName(classes.cardRotate);
    for (let i = 0; i < rotatingCards.length; i++) {
      var rotatingCard = rotatingCards[i];
      var rotatingWrapper = rotatingCard.parentElement;
      var cardWidth = rotatingCard.parentElement.offsetWidth;
      var cardHeight = rotatingCard.children[0].children[0].offsetHeight;
      rotatingWrapper.style.height = cardHeight + "px";
      rotatingWrapper.style["margin-bottom"] = 30 + "px";
      var cardFront = rotatingCard.getElementsByClassName(classes.front)[0];
      var cardBack = rotatingCard.getElementsByClassName(classes.back)[0];
      cardFront.style.height = cardHeight + 35 + "px";
      cardFront.style.width = cardWidth + "px";
      cardBack.style.height = cardHeight + 35 + "px";
      cardBack.style.width = cardWidth + "px";
    }
  }
  render() {
    const { classes, ...rest } = this.props;
    return (
      <div {...rest} className="cd-section" id="cards">
          <div className={classes.container}>
            <GridContainer>
                {
                    this.props.stareCart.map(item =>{
                        return(
                            <GridItem xs={12} sm={6} md={4}>
                                <Card blog>
                                    <CardHeader image>
                                        <a href="#pablo" onClick={e => e.preventDefault()}>
                                        <img src={item.url} alt="..." />
                                        </a>
                                        <div
                                        className={classes.coloredShadow}
                                        style={{
                                            backgroundImage: `url(${color1})`,
                                            opacity: "1"
                                        }}
                                        />
                                    </CardHeader>
                                    <CardBody>
                                        <Warning>
                                        <h6 className={classes.cardCategory}>{item.title}</h6>
                                        </Warning>
                                        <h4 className={classes.cardTitle}>
                                        <a href="#pablo" onClick={e => e.preventDefault()}>
                                            {item.text}
                                        </a>
                                        </h4>
                                        <div className={classes.textCenter}>
                                            <Button>开始预习</Button>
                                        </div>
                                        
                                    </CardBody>
                                </Card>
                            </GridItem>
                        )
                    })
                }
            </GridContainer>
          </div>
          {/* DYNAMIC COLORED SHADOWS END */}
        {/* </div> */}
       
      </div>
    );
  }
}

export default withStyles(styles)(SectionCards);

import React from "react";
// nodejs library that concatenates classes
import classNames from "classnames";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
import Tooltip from "@material-ui/core/Tooltip";
// @material-ui/icons
import Close from "@material-ui/icons/Close";
import Remove from "@material-ui/icons/Remove";
import Add from "@material-ui/icons/Add";
import KeyboardArrowRight from "@material-ui/icons/KeyboardArrowRight";
// core components
import Headers from "../components/MyHeader";
import Parallax from "../../../components/Parallax/Parallax.jsx";
import GridContainer from "../../../components/Grid/GridContainer.jsx";
import GridItem from "../../../components/Grid/GridItem.jsx";
import Footers from "../components/Footers";
import Table from "../../../components/Table/Table.jsx";
import Button from "../../../components/CustomButtons/Button.jsx";
import Card from "../../../components/Card/Card.jsx";
import CardBody from "../../../components/Card/CardBody.jsx";

import shoppingCartStyle from "../../../../assets/jss/material-kit-pro-react/views/shoppingCartStyle.jsx";

import product1 from "../../../../assets/img/product1.jpg";


class ShoppingCartPage extends React.Component {
  componentDidMount() {
    window.scrollTo(0, 0);
    document.body.scrollTop = 0;
  }
  render() {
    const { classes } = this.props;
    return (
      <div>
        <Headers/>
        <Parallax
          image={require("../../../../assets/img/examples/bg2.jpg")}
          filter="dark"
          small
        >
          <div className={classes.container}>
            <GridContainer>
              <GridItem
                md={8}
                sm={8}
                className={classNames(
                  classes.mlAuto,
                  classes.mrAuto,
                  classes.textCenter
                )}
              >
                <h2 className={classes.title}>Shopping Page</h2>
              </GridItem>
            </GridContainer>
          </div>
        </Parallax>
        <div className={classNames(classes.main, classes.mainRaised)}>
          <div className={classes.container}>
            <Card plain>
              <CardBody plain>
                <h3 className={classes.cardTitle}>购 物 车</h3>
                <Table
                  tableHead={[
                    "简介图",
                    "商品及简介",
                    "",
                    "课时",
                    "单价",
                    "数量",
                    "总计",
                    ""
                  ]}
                  tableData={[
                    [
                      <div className={classes.imgContainer}>
                        <img src={product1} alt="..." className={classes.img} />
                      </div>,
                      <span>
                        <p className={classes.tdNameAnchor}>
                          python 入门和实践
                        </p>
                        <br />
                        <small className={classes.tdNameSmall}>
                          python 从入门到实践 一步一步带你走上python智能
                        </small>
                      </span>,
                      "",
                      "240小时",
                      <span>
                        <small className={classes.tdNumberSmall}>￥</small> 549
                      </span>,
                      <span>
                        1{` `}
                        <div className={classes.buttonGroup}>
                          <Button
                            color="info"
                            size="sm"
                            round
                            className={classes.firstButton}
                          >
                            <Remove />
                          </Button>
                          <Button
                            color="info"
                            size="sm"
                            round
                            className={classes.lastButton}
                          >
                            <Add />
                          </Button>
                        </div>
                      </span>,
                      <span>
                        <small className={classes.tdNumberSmall}>￥</small> 549
                      </span>,
                      <Tooltip
                        id="close1"
                        title="Remove"
                        placement="left"
                        classes={{ tooltip: classes.tooltip }}
                      >
                        <Button link className={classes.actionButton}>
                          <Close />
                        </Button>
                      </Tooltip>
                    ],
                    {
                      purchase: true,
                      colspan: "3",
                      amount: (
                        <span>
                          <small>￥</small>2,346
                        </span>
                      ),
                      col: {
                        colspan: 3,
                        text: (
                          <Button color="info" round>
                            结算 <KeyboardArrowRight />
                          </Button>
                        )
                      }
                    }
                  ]}
                  tableShopping
                  customHeadCellClasses={[
                    classes.textCenter,
                    classes.description,
                    classes.description,
                    classes.textRight,
                    classes.textRight,
                    classes.textRight
                  ]}
                  customHeadClassesForCells={[0, 2, 3, 4, 5, 6]}
                  customCellClasses={[
                    classes.tdName,
                    classes.customFont,
                    classes.customFont,
                    classes.tdNumber,
                    classes.tdNumber + " " + classes.tdNumberAndButtonGroup,
                    classes.tdNumber + " " + classes.textCenter
                  ]}
                  customClassesForCells={[1, 2, 3, 4, 5, 6]}
                />
              </CardBody>
            </Card>
          </div>
        </div>
        <Footers/>
      </div>
    );
  }
}

export default withStyles(shoppingCartStyle)(ShoppingCartPage);

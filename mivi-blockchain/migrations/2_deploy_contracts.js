const MIVIConsultation = artifacts.require("./MIVIConsultation");

module.exports = function(deployer) {
  deployer.deploy(MIVIConsultation);
};
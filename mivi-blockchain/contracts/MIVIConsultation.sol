pragma solidity ^0.8.0;

contract MIVIConsultation {
    struct Consultation {
        string patientName;
        uint256 age;
        string gender;
        string symptoms;
        string aiResponse;
        uint256 timestamp;
    }
    
    mapping(address => Consultation[]) private patientConsultations;
    
    event ConsultationAdded(address indexed patient, uint256 timestamp);
    
    function addConsultation(
        string memory _patientName,
        uint256 _age,
        string memory _gender,
        string memory _symptoms,
        string memory _aiResponse
    ) public {
        Consultation memory newConsultation = Consultation({
            patientName: _patientName,
            age: _age,
            gender: _gender,
            symptoms: _symptoms,
            aiResponse: _aiResponse,
            timestamp: block.timestamp
        });
        
        patientConsultations[msg.sender].push(newConsultation);
        emit ConsultationAdded(msg.sender, block.timestamp);
    }
    
    function getConsultations() public view returns (Consultation[] memory) {
        return patientConsultations[msg.sender];
    }
}
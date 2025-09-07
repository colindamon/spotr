import React from 'react';
import { Card, ListGroup } from 'react-bootstrap';

const CarSpecs = ({ specs }) => {
  if (!specs) return null;

  return (
    <Card className="shadow-sm">
      <Card.Body>
        <h4 className="text-center mb-3">Car Specifications</h4>
        <ListGroup variant="flush">
          {Object.entries(specs).map(([key, value]) => (
            <ListGroup.Item key={key} className="d-flex justify-content-between">
              <strong>{key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}:</strong>
              <span>{value || 'N/A'}</span>
            </ListGroup.Item>
          ))}
        </ListGroup>
      </Card.Body>
    </Card>
  );
};

export default CarSpecs;

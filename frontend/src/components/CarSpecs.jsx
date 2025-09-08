import React from 'react';
import { Card, ListGroup } from 'react-bootstrap';

const CarSpecs = ({ specs }) => {
  if (!specs) return null;

  return (
    <Card className="shadow-sm" style={{
      backgroundColor: 'var(--bg-card)',
      borderColor: 'var(--border-color)',
      color: 'var(--text-primary)'
    }}>
      <Card.Body>
        <h4 className="text-center mb-3" style={{ color: 'var(--text-primary)' }}>
          🔧 Car Specifications
        </h4>
        <ListGroup variant="flush">
          {Object.entries(specs).map(([key, value]) => (
            <ListGroup.Item 
              key={key} 
              className="d-flex justify-content-between"
              style={{
                backgroundColor: 'var(--bg-card)',
                borderColor: 'var(--border-color)',
                color: 'var(--text-primary)'
              }}
            >
              <strong style={{ color: 'var(--text-secondary)' }}>
                {key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}:
              </strong>
              <span style={{ color: 'var(--text-primary)' }}>
                {value || 'N/A'}
              </span>
            </ListGroup.Item>
          ))}
        </ListGroup>
      </Card.Body>
    </Card>
  );
};

export default CarSpecs;

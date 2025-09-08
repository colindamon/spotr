import React from 'react';
import { Card, Button, Spinner } from 'react-bootstrap';

const CarResult = ({ predClass, onShowSpecs, specLoading }) => {
  if (!predClass) return null;

  return (
    <Card className="shadow-sm mb-4" style={{
      backgroundColor: 'var(--bg-card)',
      borderColor: 'var(--border-color)',
      color: 'var(--text-primary)'
    }}>
      <Card.Body>
        <h4 className="text-center mb-3" style={{ color: 'var(--success)' }}>
          🎉 Car Identified!
        </h4>
        <p className="text-center lead" style={{ 
          fontSize: '1.25rem', 
          fontWeight: '600',
          color: 'var(--text-primary)',
          margin: '1rem 0'
        }}>
          {predClass}
        </p>
        <div className="d-flex justify-content-center">
          <Button
            variant="info"
            onClick={onShowSpecs}
            disabled={specLoading}
            style={{
              backgroundColor: 'var(--info)',
              borderColor: 'var(--info)',
              color: 'white'
            }}
          >
            {specLoading ? (
              <>
                <Spinner as="span" animation="border" size="sm" className="me-2" />
                Loading specs...
              </>
            ) : (
              '📋 Show Specifications'
            )}
          </Button>
        </div>
      </Card.Body>
    </Card>
  );
};

export default CarResult;

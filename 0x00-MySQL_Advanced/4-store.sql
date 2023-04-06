-- Create a new trigger named 'decrease_quantity'
CREATE TRIGGER decrease_quantity BEFORE INSERT ON orders 
FOR EACH ROW UPDATE items
    -- Less the quantity of the item following the order from the 'quantity' column in the 'items' table
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;

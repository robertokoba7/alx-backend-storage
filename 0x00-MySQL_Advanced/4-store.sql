-- Create a new trigger named 'decrease_quantity'
CREATE TRIGGER decrease_quantity
-- Set trigger to activate after an INSERT into the 'orders' table
AFTER INSERT ON orders 
FOR EACH ROW
BEGIN
    -- Less the quantity of the item following the order from the 'quantity' column in the 'items' table
    UPDATE items SET quantity = quantity - NEW.quantity WHERE id = NEW.item_id;
END;

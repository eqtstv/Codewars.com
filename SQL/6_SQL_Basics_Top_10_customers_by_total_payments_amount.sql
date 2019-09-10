select c.customer_id, c.email, count(p.payment_id) payments_count, cast(sum(p.amount) as float) total_amount
from customer c join payment p on c.customer_id = p.customer_id
group by c.customer_id
order by total_amount DESC
limit 10;
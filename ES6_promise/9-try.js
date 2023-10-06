export default function guardrail(mathFunction) {
  const queue = [];
  let result;

  try {
    result = mathFunction();
    queue.push(result);
  } catch (error) {
    queue.push(error.message);
  }
  queue.push('Guardrail was processed');

  return queue;
}

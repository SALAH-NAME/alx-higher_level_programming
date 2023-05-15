#include "lists.h"
#include <stddef.h>

listint_t *add_nodeint_start(listint_t **head, const int n)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = (*head);
	(*head) = new;

	return (*head);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *stack = NULL;
	listint_t *b_stack = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (current != NULL)
	{
		add_nodeint_start(&stack, current->n);
		current = current->next;
	}

	current = *head;
	b_stack = stack;

	while (current != NULL)
	{
		if (current->n != b_stack->n)
		{
			free_listint(stack);
			return (0);
		}
		current = current->next;
		b_stack = b_stack->next;
	}
	free_listint(stack);
	return (1);
}

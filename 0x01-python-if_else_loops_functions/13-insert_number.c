#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: node head
 * @number: the num to stored
 * 
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_set = malloc(sizeof(listint_t));
	listint_t *current;

	current = *head;

	if (new_set == NULL)
		return (NULL);

	new_set->n = number;

	if (number < current->n)
	{
		new_set->next = (*head);
		(*head) = new_set;
	}
	else
	{
		while (current->next != NULL)
		{
			if (number >= current->n && number <= current->next->n)
			{
				new_set->next = current->next;
				current->next = new_set;
				break;
			}
			current = current->next;
		}
	}
	return (new_set);
}

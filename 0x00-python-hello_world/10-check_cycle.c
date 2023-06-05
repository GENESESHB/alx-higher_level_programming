#include "lists.h"
/**
 *check_cycle - a function that checks if there is a loop or not.
 *@list: a pointer to the head of the linked list.
 *Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL;
	listint_t *slow = NULL;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (slow && fast && fast->next)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

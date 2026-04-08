---
id: aaa-example
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:39.307987
---

# AAA Structure Example

Every test must follow Arrange-Act-Assert:

```typescript
it('should return user by ID', async () => {
  // Arrange
  const userId = 'abc-123';
  const expected = { id: userId, name: 'Alice' };
  userRepo.findById.mockResolvedValue(expected);

  // Act
  const result = await userService.getById(userId);

  // Assert
  expect(result).toEqual(expected);
});
```

---
id: auth-logic
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:51.150121
---

# Child Access Authorization Logic

All child-specific services must call `childrenService.validateChildAccess()` to prevent ID-guessing attacks (Insecure Direct Object Reference). This method is centralized in `ChildrenService`.

## Centralized Method in `ChildrenService`

```typescript
public async validateChildAccess(childId: string, userId: string): Promise<void> {
  const membership = await this.familyMemberRepository.findOne({
    where: { child: { id: childId }, user: { id: userId } },
    relations: ['family'],
  });

  if (!membership) {
    // Fallback: check if they are in the family that owns the child
    const child = await this.childRepository.findOne({
      where: { id: childId },
      relations: ['family'],
    });

    if (!child) throw new NotFoundException('Child not found');

    const familyMembership = await this.familyMemberRepository.findOne({
      where: { family: { id: child.family.id }, user: { id: userId } },
    });

    if (!familyMembership) throw new ForbiddenException('Access denied');
  }
}
```

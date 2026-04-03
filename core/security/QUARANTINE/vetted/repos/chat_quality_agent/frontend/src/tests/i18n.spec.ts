import { describe, it, expect } from 'vitest'
import vi from '../i18n/vi'
import en from '../i18n/en'

describe('i18n completeness', () => {
  const viKeys = Object.keys(vi).sort()
  const enKeys = Object.keys(en).sort()

  it('should have the same number of keys in vi and en', () => {
    expect(viKeys.length).toBe(enKeys.length)
  })

  it('all vi keys should exist in en', () => {
    const missingInEn = viKeys.filter((key) => !enKeys.includes(key))
    expect(missingInEn).toEqual([])
  })

  it('all en keys should exist in vi', () => {
    const missingInVi = enKeys.filter((key) => !viKeys.includes(key))
    expect(missingInVi).toEqual([])
  })

  it('no empty values in vi', () => {
    const emptyVi = viKeys.filter((key) => !(vi as Record<string, string>)[key])
    expect(emptyVi).toEqual([])
  })

  it('no empty values in en', () => {
    const emptyEn = enKeys.filter((key) => !(en as Record<string, string>)[key])
    expect(emptyEn).toEqual([])
  })
})

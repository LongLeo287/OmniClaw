---
id: github.com-deltazero-cz-node-isdoc-pdf-f5f5948f-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:44.337604
---

# KNOWLEDGE EXTRACT: github.com_deltazero-cz_node-isdoc-pdf_f5f5948f
> **Extracted on:** 2026-04-01 13:21:28
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007522382/github.com_deltazero-cz_node-isdoc-pdf_f5f5948f

---

## File: `.gitignore`
```
/node_modules
/.idea
*.d.ts
*.js
```

## File: `.npmignore`
```
.idea
.env
*.ts
!*.d.ts
*.tgz
```

## File: `LICENSE`
```
ISC License

Copyright 2022 David Obdržálek [delta zero]

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## File: `README.md`
```markdown
# ISDOC-PDF Node.js library

[ISDOC](https://isdoc.github.io/) is an XML Invoicing Standard for the Czech Republic.

This library can:
- extract ISDOC invoices from PDFs
- create ISDOC.PDF (PDF/A-3B with ISDOC attached)
- create IDDOCX archives (zips with PDF and ISDOC)

It also provides Node.js API for ISDOC format, see [node-isdoc](https://github.com/deltazero-cz/node-isdoc),
incl. XSD xchema validation.

### Installation

```shell
npm i isdoc-pdf
```

To create ISDOC.PDF (PDF/A-3B with ISDOC attached),
this package depends on Bash-like shell and Ghostscript,
see [isdoc-pdf (bash)](https://github.com/deltazero-cz/isdoc-pdf).

### Usage

Extract ISDOC from existing PDF

```js
import { hasISDOC, extractISDOC } from 'isdoc-pdf'

const plainInvoice = await fs.readFile('invoice.pdf'),
      isdocInvoice = await fs.readFile('invoice.isdoc.pdf')

await hasISDOC(plainInvoice)
// -> false

await hasISDOC(isdocInvoice)
// -> true

await extractISDOC(plainInvoice)
// -> null 

await extractISDOC(isdocInvoice)
// -> Invoice { DocumentType: number, ID: string, IssueDate: Date, ... }
```

Create ISDOC.PDF (attach ISDOC to PDF and convert into PDF/A-3)

```js
import { attachISDOC } from 'isdoc-pdf'

const invoice = await fs.readFile('invoice.pdf'),
      isdoc = await fs.readFile('invoice.isdoc')

const pdfa = await attachISDOC(invoice, isdoc)
// -> Buffer with PDF/A-3
```

Create ISDOC.PDF with a new Invoice

```js
import { Invoice, attachISDOC } from 'isdoc-pdf'

const isdoc = new Invoice({
  DocumentType: 1,
  ID: '2022123456',
  ... // see https://github.com/deltazero-cz/node-isdoc
})

const pdf = await fs.readFile('invoice.pdf')

const pdfa = await attachISDOC(pdf, isdoc)
// -> Buffer with PDF/A-3
```

Create IDDOCX archives (ZIP archives with PDF and ISDOC)

```js
import { createISDOCX } from 'isdoc-pdf'

const invoice = await fs.readFile('invoice.pdf'),
      isdoc = await fs.readFile('invoice.isdoc')

const isdocx = await createISDOCX(invoice, invoice)
// -> Buffer with ISDOCX (ZIP archive)
```

Create IDDOCX with a new Invoice

```js
import { Invoice, createISDOCX } from 'isdoc-pdf'

const isdoc = new Invoice({
  DocumentType: 1,
  ID: '2022123456',
  ... // see https://github.com/deltazero-cz/node-isdoc
})

const pdf = await fs.readFile('invoice.pdf')

const isdocx = await createISDOCX(pdf, isdoc)
// -> Buffer with ISDOCX (ZIP archive)
```
```

## File: `index.ts`
```typescript
import Invoice, { InvoiceType } from '@deltazero/isdoc'
import extractISDOC, { hasISDOC } from './lib/extractISDOC'
import createISDOCX from './lib/createISDOCX'
import attachISDOC from './lib/attachISDOC'

export { Invoice, InvoiceType, createISDOCX, attachISDOC, extractISDOC, hasISDOC }
```

## File: `package.json`
```json
{
  "name": "isdoc-pdf",
  "version": "0.1.2",
  "description": "Create ISDOC.PDF (PDF/A-3 with ISDOC attachment), create ISDOCX (ZIP archive with PDF and ISDOC) or extract ISDOC from PDF - Czechia's standard invoice format for data exchange",
  "author": "ΔO - David Obdržálek <david@deltazero.cz>",
  "license": "ISC",
  "keywords": [
    "isdoc",
    "isdocx",
    "isdoc-pdf",
    "pdf",
    "pdfa",
    "pdf/a",
    "pdf/a-3"
  ],
  "main": "index.js",
  "types": "index.d.ts",
  "scripts": {
    "pretest": "tsc",
    "test": "mocha tests --timeout 10000",
    "build": "tsc -b",
    "prepare": "npm run build"
  },
  "repository": "deltazero-cz/node-isdoc",
  "engines": {
    "node": ">=14.0.0"
  },
  "dependencies": {
    "@deltazero/isdoc": "^0.1.2",
    "jszip": "^3.10.1",
    "pdf-lib": "^1.17.1",
    "xsd-validator": "^1.1.0",
    "isdoc-pdf-bash": "git+https://github.com/deltazero-cz/isdoc-pdf.git"
  },
  "devDependencies": {
    "@types/chai": "^4.3.3",
    "@types/mocha": "^9.1.1",
    "@types/node": "^16.0.0",
    "chai": "^4.3.6",
    "mocha": "^10.0.0",
    "typescript": "latest"
  }
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "lib": ["es2020"],
    "module": "commonjs",
    "target": "es2020",
    "declaration": false,
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node"
  },

  "exclude": [
    "node_modules"
  ]
}
```

## File: `lib/PDFAttachments.ts`
```typescript
import {
  PDFDocument,
  PDFName,
  PDFDict,
  PDFArray,
  PDFHexString,
  PDFString,
  PDFStream,
  decodePDFRawStream,
  PDFRawStream,
} from 'pdf-lib'

export const PDFExtractAttachments = (pdfDoc: PDFDocument) => {
  const rawAttachments = PDFExtractRawAttachments(pdfDoc)
  return rawAttachments.map(({ fileName, fileSpec }) => {
    const stream = fileSpec
        .lookup(PDFName.of('EF'), PDFDict)
        .lookup(PDFName.of('F'), PDFStream) as PDFRawStream
    return {
      name: fileName.decodeText(),
      data: decodePDFRawStream(stream).decode(),
    }
  })
}

export const PDFExtractRawAttachments = (pdfDoc: PDFDocument) => {
  if (!pdfDoc.catalog.has(PDFName.of('Names'))) return []
  const Names = pdfDoc.catalog.lookup(PDFName.of('Names'), PDFDict)

  if (!Names.has(PDFName.of('EmbeddedFiles'))) return []
  let EmbeddedFiles = Names.lookup(PDFName.of('EmbeddedFiles'), PDFDict)

  if (!EmbeddedFiles.has(PDFName.of('Names')) && EmbeddedFiles.has(PDFName.of('Kids')))
    EmbeddedFiles = EmbeddedFiles.lookup(PDFName.of('Kids'), PDFArray).lookup(0) as PDFDict

  if (!EmbeddedFiles.has(PDFName.of('Names'))) return []
  const EFNames = EmbeddedFiles.lookup(PDFName.of('Names'), PDFArray)

  const rawAttachments = []
  for (let idx = 0, len = EFNames.size(); idx < len; idx += 2) {
    const fileName = EFNames.lookup(idx) as PDFHexString | PDFString
    const fileSpec = EFNames.lookup(idx + 1, PDFDict)
    rawAttachments.push({ fileName, fileSpec })
  }

  return rawAttachments
}
```

## File: `lib/attachISDOC.ts`
```typescript
import Invoice, {InvoiceType} from '@deltazero/isdoc'
import { PDFDocument } from 'pdf-lib'
import { hasISDOC } from './extractISDOC'
import { readFile, writeFile, stat, unlink } from 'fs/promises'
import { exec } from 'child_process'

export default async function attachISDOC(
    pdf: Buffer|PDFDocument,
    isdoc: string|Buffer|Invoice|InvoiceType
) : Promise<Buffer> {
  if (await hasISDOC(pdf))
    throw new Error('attachISDOC: This PDF Already Has an ISDOC Attachment')

  if (!(isdoc instanceof Invoice))
    isdoc = new Invoice(isdoc)

  if (pdf instanceof PDFDocument)
    pdf = Buffer.from(await pdf.save())

  const bin = __dirname + '/../node_modules/isdoc-pdf-bash/isdoc-pdf'
  await stat(bin)
    .catch(() => { throw new Error('attachISDOC: Cannot find [isdoc-pdf] executable') })

  const [[ inpdf ], [ inisdoc ], [ outpdf ]] = await Promise.all([ execute('mktemp'), execute('mktemp'), execute('mktemp') ])
  await Promise.all([
      writeFile(inpdf, pdf),
      writeFile(inisdoc, isdoc.toXML())
  ])

  await execute(`${bin} ${inpdf} ${inisdoc} ${outpdf}`)
  const result = await readFile(outpdf)

  // clean up
  await Promise.all([ unlink(inpdf), unlink(inisdoc), unlink(outpdf) ])

  return result
}

const execute = async (cmd: string, options: any = {}) : Promise<[string, string?]> =>
    new Promise((resolve, reject) =>
      exec(cmd, options, (e, stdout, stderr) => {
        if (e) return reject(e)
        resolve([stdout.toString().trim(), stderr?.toString().trim()])
      })
    )
```

## File: `lib/createISDOCX.ts`
```typescript
import Invoice, { InvoiceType } from '@deltazero/isdoc'
import Zip from 'jszip'
import { hasISDOC } from './extractISDOC'

export default async function createISDOCX(
    pdf: Buffer,
    isdoc: string|Buffer|Invoice|InvoiceType,
    name ?: string
) {
  // noinspection SuspiciousTypeOfGuard
  if (!(pdf instanceof Buffer))
    throw new Error('createISDOCX: PDF Is Not an Instance of Buffer')

  if (await hasISDOC(pdf))
    throw new Error('createISDOCX: This PDF Already Has an ISDOC Attachment')

  if (!(isdoc instanceof Invoice))
    isdoc = new Invoice(isdoc)

  name ??= isdoc.ID?.replace(/[^\w.-]/gi, '_')
  if (!name)
    throw new Error('createISDOCX: File Name Is Not Set')

  const zip = new Zip()
  zip.file(name + '.pdf', pdf)
  zip.file(name + '.isdoc', isdoc.toXML())
  zip.file('manifest.xml', createManifest(name))

  return zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' })
}

export const createManifest = (name: string) : string =>
`<?xml version="1.0"?>
<manifest xmlns="http://isdoc.cz/namespace/2013/manifest">
  <maindocument filename="${name}.isdoc"/>
</manifest>
`
```

## File: `lib/extractISDOC.ts`
```typescript
import PDFDocument from 'pdf-lib/cjs/api/PDFDocument'
import { PDFExtractAttachments } from './PDFAttachments'
import Invoice from '@deltazero/isdoc'

export default async function extractISDOC(pdf: Buffer|PDFDocument) : Promise<Invoice|null> {
  const document = !(pdf instanceof PDFDocument)
      ? await PDFDocument.load(pdf)
      : pdf

  const isdoc = PDFExtractAttachments(document)
      .find(r => r.name.match(/isdoc$/))
  if (!isdoc) return null

  return new Invoice(Buffer.from(isdoc.data))
}

export const hasISDOC = async (pdf: Buffer|PDFDocument) : Promise<boolean> => {
  const document = !(pdf instanceof PDFDocument)
      ? await PDFDocument.load(pdf)
      : pdf

  return !! PDFExtractAttachments(document).find(r => r.name.match(/isdoc$/))
}
```

## File: `lib/schemaISDOC.ts`
```typescript
export default `<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="http://isdoc.cz/namespace/2013" xmlns:isdoc="http://isdoc.cz/namespace/2013" targetNamespace="http://isdoc.cz/namespace/2013" elementFormDefault="qualified" version="6.0.2" xml:lang="cs">
  <xs:group name="Signature">
    <xs:sequence>
      <xs:any namespace="http://www.w3.org/2000/09/xmldsig#" processContents="lax"/>
    </xs:sequence>
  </xs:group>

  <xs:simpleType name="VersionType">
    <xs:restriction base="xs:string">
      <xs:pattern value="[0-9]+\\.[0-9]+(\\.[0-9]+)?"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="DocumentTypeType">
    <xs:restriction base="xs:integer">
      <xs:enumeration value="1">
        </xs:enumeration>
      <xs:enumeration value="2">
        </xs:enumeration>
      <xs:enumeration value="3">
        </xs:enumeration>
      <xs:enumeration value="4">
        </xs:enumeration>
      <xs:enumeration value="5">
        </xs:enumeration>
      <xs:enumeration value="6">
        </xs:enumeration>
      <xs:enumeration value="7">
        </xs:enumeration>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="SubDocumentTypeType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="SubDocumentTypeOriginType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>
  
  <xs:simpleType name="TargetConsolidatorType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="ClientOnTargetConsolidatorType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>
  
  <xs:simpleType name="ClientBankAccountType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="IDType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="ID36Type">
    <xs:restriction base="IDType">
      <xs:maxLength value="36"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="UUIDType">
    <xs:restriction base="xs:string">
      <xs:pattern value="[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="IDSchemeType">
    <xs:restriction base="xs:anyURI"/>
  </xs:simpleType>

  <xs:simpleType name="IssuingSystemType">
    <xs:restriction base="xs:string">
      <xs:maxLength value="80"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="IssueDateType">
    <xs:restriction base="xs:date"/>
  </xs:simpleType>

  <xs:simpleType name="TaxPointDateType">
    <xs:restriction base="xs:date"/>
  </xs:simpleType>

  <xs:simpleType name="VATApplicableType">
    <xs:restriction base="BooleanType"/>
  </xs:simpleType>

  <xs:complexType name="NoteType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="languageID" type="xs:language" use="optional">
          </xs:attribute>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>

  <xs:complexType name="OrderReferencesType">
    <xs:sequence>
      <xs:element name="OrderReference" type="OrderReferenceType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="OrderReferenceType">
    <xs:sequence>
      <xs:element name="SalesOrderID" type="SalesOrderIDType">
        </xs:element>
      <xs:element name="ExternalOrderID" type="IDType" minOccurs="0">
        </xs:element>
      <xs:element name="IssueDate" type="IssueDateType" minOccurs="0">
        </xs:element>
      <xs:element name="ExternalOrderIssueDate" type="IssueDateType" minOccurs="0">
        </xs:element>
      <xs:element name="UUID" type="UUIDType" minOccurs="0">
        </xs:element>
      <xs:element name="ISDS_ID" type="ISDS_IDType" minOccurs="0">
        </xs:element>
      <xs:element name="FileReference" type="FileReferenceType" minOccurs="0">
        </xs:element>
      <xs:element name="ReferenceNumber" type="ReferenceNumberType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="IdAttribute"/>
  </xs:complexType>

  <xs:complexType name="OrderLineReferenceType">
    <xs:sequence>
      <xs:element name="LineID" type="LineIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="RefAttribute"/>
  </xs:complexType>

  <xs:simpleType name="SalesOrderIDType">
    <xs:restriction base="IDType"/>
  </xs:simpleType>

  <xs:simpleType name="LineIDType">
    <xs:restriction base="IDType"/>
  </xs:simpleType>

  <xs:simpleType name="ParagraphIDType">
    <xs:restriction base="IDType"/>
  </xs:simpleType>

  <xs:complexType name="DeliveryNoteReferencesType">
    <xs:sequence>
      <xs:element name="DeliveryNoteReference" type="DeliveryNoteReferenceType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="DeliveryNoteReferenceType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
      <xs:element name="IssueDate" type="IssueDateType" minOccurs="0">
        </xs:element>
      <xs:element name="UUID" type="UUIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="IdAttribute"/>
  </xs:complexType>

  <xs:complexType name="DeliveryNoteLineReferenceType">
    <xs:sequence>
      <xs:element name="LineID" type="LineIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="RefAttribute"/>
  </xs:complexType>

  <xs:complexType name="ContractReferencesType">
    <xs:sequence>
      <xs:element name="ContractReference" type="ContractReferenceType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="ContractReferenceType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
      <xs:element name="UUID" type="UUIDType" minOccurs="0">
        </xs:element>
      <xs:element name="IssueDate" type="IssueDateType">
        </xs:element>
      <xs:choice minOccurs="0">
        <xs:element name="LastValidDate" type="LastValidDateType">
          </xs:element>
        <xs:element name="LastValidDateUnbounded" type="LastValidDateUnboundedType">
          </xs:element>
      </xs:choice>
      <xs:element name="ISDS_ID" type="ISDS_IDType" minOccurs="0">
        </xs:element>
      <xs:element name="FileReference" type="FileReferenceType" minOccurs="0">
        </xs:element>
      <xs:element name="ReferenceNumber" type="ReferenceNumberType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="IdAttribute"/>
  </xs:complexType>

  <xs:complexType name="ContractLineReferenceType">
    <xs:sequence>
      <xs:element name="ParagraphID" type="ParagraphIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="RefAttribute"/>
  </xs:complexType>

  <xs:simpleType name="LastValidDateType">
    <xs:restriction base="xs:date"/>
  </xs:simpleType>

  <xs:complexType name="LastValidDateUnboundedType">
    </xs:complexType>

  <xs:simpleType name="CurrRateType">
    <xs:restriction base="xs:decimal"/>
  </xs:simpleType>

  <xs:simpleType name="RefCurrRateType">
    <xs:restriction base="xs:decimal"/>
  </xs:simpleType>

  <xs:complexType name="OriginalDocumentReferencesType">
    <xs:sequence>
      <xs:element name="OriginalDocumentReference" type="OriginalDocumentReferenceType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="OriginalDocumentReferenceType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
      <xs:element name="IssueDate" type="IssueDateType" minOccurs="0">
        </xs:element>
      <xs:element name="UUID" type="UUIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="IdAttribute"/>
  </xs:complexType>

  <xs:complexType name="OriginalDocumentLineReferenceType">
    <xs:sequence>
      <xs:element name="LineID" type="LineIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="RefAttribute"/>
  </xs:complexType>

  <xs:complexType name="SupplementsListType">
    <xs:sequence>
      <xs:element maxOccurs="unbounded" name="Supplement" type="SupplementType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="SupplementType">
    <xs:sequence>
      <xs:element name="Filename" type="FilenameType">
        </xs:element>
      <xs:element name="DigestMethod" type="DigestMethodType">
        </xs:element>
      <xs:element name="DigestValue" type="DigestValueType">
        </xs:element>
    </xs:sequence>
    <xs:attribute name="preview" type="BooleanType">
      </xs:attribute>
  </xs:complexType>

  <xs:simpleType name="FilenameType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="DigestMethodType">
    <xs:attribute name="Algorithm" use="required" type="xs:anyURI">
      </xs:attribute>
  </xs:complexType>

  <xs:simpleType name="DigestValueType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="BooleanType">
    <xs:restriction base="xs:boolean">
      <xs:pattern value="true|false"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="ExtensionsType">
    <xs:sequence>
      <xs:any minOccurs="1" maxOccurs="unbounded" namespace="##other" processContents="lax"/>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="AccountingSupplierPartyType">
    <xs:sequence>
      <xs:element name="Party" type="PartyType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="PartyType">
    <xs:sequence>
      <xs:element name="PartyIdentification" type="PartyIdentificationType">
        </xs:element>
      <xs:element name="PartyName" type="PartyNameType">
        </xs:element>
      <xs:element name="PostalAddress" type="PostalAddressType">
        </xs:element>
      <xs:element name="PartyTaxScheme" type="PartyTaxSchemeType" minOccurs="0" maxOccurs="unbounded">
        </xs:element>
      <xs:element minOccurs="0" name="RegisterIdentification" type="RegisterIdentificationType">
        </xs:element>
      <xs:element name="Contact" type="ContactType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="PartyIdentificationType">
    <xs:sequence>
      <xs:element name="UserID" type="UserIDType" minOccurs="0">
        </xs:element>
      <xs:element name="CatalogFirmIdentification" type="CatalogFirmIdentificationType" minOccurs="0">
        </xs:element>
      <xs:element name="ID" type="IDType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="UserIDType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="CatalogFirmIdentificationType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="PartyNameType">
    <xs:sequence>
      <xs:element name="Name" type="NameType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="NameType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="PostalAddressType">
    <xs:sequence>
      <xs:element name="StreetName" type="StreetNameType">
        </xs:element>
      <xs:element name="BuildingNumber" type="BuildingNumberType">
        </xs:element>
      <xs:element name="CityName" type="CityNameType">
        </xs:element>
      <xs:element name="PostalZone" type="PostalZoneType">
        </xs:element>
      <xs:element name="Country" type="CountryType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="StreetNameType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="BuildingNumberType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="CityNameType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="PostalZoneType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="CountryType">
    <xs:sequence>
      <xs:element name="IdentificationCode" type="IdentificationCodeType">
        </xs:element>
      <xs:element name="Name" type="NameType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="IdentificationCodeType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="PartyTaxSchemeType">
    <xs:sequence>
      <xs:element name="CompanyID" type="CompanyIDType">
        </xs:element>
      <xs:element name="TaxScheme" type="TaxSchemeType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="CompanyIDType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="TaxSchemeType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="RegisterIdentificationType">
    <xs:choice>
      <xs:sequence>
        <xs:element name="RegisterKeptAt" type="RegisterKeptAtType">
          </xs:element>
        <xs:element name="RegisterFileRef" type="RegisterFileRefType">
          </xs:element>
        <xs:element name="RegisterDate" type="RegisterDateType">
          </xs:element>
      </xs:sequence>
      <xs:element name="Preformatted" type="PreformattedType">
        </xs:element>
    </xs:choice>
  </xs:complexType>

  <xs:simpleType name="RegisterKeptAtType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="RegisterFileRefType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="RegisterDateType">
    <xs:restriction base="xs:date"/>
  </xs:simpleType>

  <xs:simpleType name="PreformattedType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="ContactType">
    <xs:sequence>
      <xs:element name="Name" type="NameType" minOccurs="0">
        </xs:element>
      <xs:element name="Telephone" type="TelephoneType" minOccurs="0">
        </xs:element>
      <xs:element name="ElectronicMail" type="ElectronicMailType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="TelephoneType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="ElectronicMailType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="SellerSupplierPartyType">
    <xs:sequence>
      <xs:element name="Party" type="PartyType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="AccountingCustomerPartyType">
    <xs:sequence>
      <xs:element name="Party" type="PartyType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="AnonymousCustomerPartyType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
      <xs:element name="IDScheme" type="IDSchemeType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="BuyerCustomerPartyType">
    <xs:sequence>
      <xs:element name="Party" type="PartyType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="DeliveryType">
    <xs:sequence>
      <xs:element name="Party" type="PartyType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="InvoiceLinesType">
    <xs:sequence>
      <xs:element maxOccurs="unbounded" name="InvoiceLine" type="InvoiceLineType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="InvoiceLineType">
    <xs:sequence>
      <xs:element name="ID" type="ID36Type">
        </xs:element>
      <xs:element name="OrderReference" type="OrderLineReferenceType" minOccurs="0">
        </xs:element>
      <xs:element name="DeliveryNoteReference" type="DeliveryNoteLineReferenceType" minOccurs="0">
        </xs:element>
      <xs:element name="OriginalDocumentReference" type="OriginalDocumentLineReferenceType" minOccurs="0">
        </xs:element>
      <xs:element name="ContractReference" type="ContractLineReferenceType" minOccurs="0">
        </xs:element>
      <xs:element name="EgovClassifier" type="EgovClassifierType" minOccurs="0">
        </xs:element>
      <xs:element name="InvoicedQuantity" type="QuantityType" minOccurs="0">
        </xs:element>
      <xs:element name="LineExtensionAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="LineExtensionAmount" type="AmountType">
        </xs:element>
      <xs:element name="LineExtensionAmountBeforeDiscount" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="LineExtensionAmountTaxInclusiveCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="LineExtensionAmountTaxInclusive" type="AmountType">
        </xs:element>
      <xs:element name="LineExtensionAmountTaxInclusiveBeforeDiscount" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="LineExtensionTaxAmount" type="AmountType">
        </xs:element>
      <xs:element name="UnitPrice" type="AmountType">
        </xs:element>
      <xs:element name="UnitPriceTaxInclusive" type="AmountType">
        </xs:element>
      <xs:element name="ClassifiedTaxCategory" type="ClassifiedTaxCategoryType">
        </xs:element>
      <xs:element name="Note" type="NoteType" minOccurs="0">
        </xs:element>
      <xs:element name="VATNote" type="NoteType" minOccurs="0">
        </xs:element>
      <xs:element name="Item" type="ItemType" minOccurs="0">
        </xs:element>
      <xs:element name="Extensions" type="ExtensionsType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="QuantityType">
    <xs:simpleContent>
      <xs:extension base="xs:decimal">
        <xs:attribute name="unitCode" use="optional" type="xs:string">
          </xs:attribute>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>

  <xs:simpleType name="CurrencyCodeType">
    <xs:restriction base="xs:string">
      <xs:length value="3"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="AmountType">
    <xs:restriction base="xs:decimal"/>
  </xs:simpleType>

  <xs:complexType name="ClassifiedTaxCategoryType">
    <xs:sequence>
      <xs:element name="Percent" type="PercentType">
        </xs:element>
      <xs:element name="VATCalculationMethod" type="VATCalculationMethodType">
        </xs:element>
      <xs:element name="VATApplicable" type="VATApplicableType" minOccurs="0">
        </xs:element>
      <xs:element name="LocalReverseCharge" type="LocalReverseChargeType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="PercentType">
    <xs:restriction base="xs:decimal"/>
  </xs:simpleType>

  <xs:simpleType name="VATCalculationMethodType">
    <xs:restriction base="xs:integer">
      <xs:enumeration value="0">
        </xs:enumeration>
      <xs:enumeration value="1">
        </xs:enumeration>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="LocalReverseChargeType">
    <xs:sequence>
      <xs:element name="LocalReverseChargeCode" type="LocalReverseChargeCodeType">
        </xs:element>
      <xs:element name="LocalReverseChargeQuantity" type="QuantityType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="LocalReverseChargeCodeType">
    <xs:union>
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="1">
            </xs:enumeration>
          <xs:enumeration value="2">
            </xs:enumeration>
          <xs:enumeration value="4">
            </xs:enumeration>
          <xs:enumeration value="5">
            </xs:enumeration>
        </xs:restriction>
      </xs:simpleType>
      <xs:simpleType>
        <xs:restriction base="xs:string"/>
      </xs:simpleType>
    </xs:union>
  </xs:simpleType>

  <xs:complexType name="ItemType">
    <xs:sequence>
      <xs:element name="Description" type="DescriptionType" minOccurs="0">
        </xs:element>
      <xs:element name="CatalogueItemIdentification" type="CatalogueItemIdentificationType" minOccurs="0">
        </xs:element>
      <xs:element name="SellersItemIdentification" type="SellersItemIdentificationType" minOccurs="0">
        </xs:element>
      <xs:element name="SecondarySellersItemIdentification" type="SecondarySellersItemIdentificationType" minOccurs="0">
        </xs:element>
      <xs:element name="TertiarySellersItemIdentification" type="TertiarySellersItemIdentificationType" minOccurs="0">
        </xs:element>
      <xs:element name="BuyersItemIdentification" type="BuyersItemIdentificationType" minOccurs="0">
        </xs:element>
      <xs:element name="StoreBatches" type="StoreBatchesType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="DescriptionType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="CatalogueItemIdentificationType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="SellersItemIdentificationType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="SecondarySellersItemIdentificationType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="TertiarySellersItemIdentificationType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="BuyersItemIdentificationType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="StoreBatchesType">
    <xs:sequence>
      <xs:element name="StoreBatch" type="StoreBatchType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="StoreBatchType">
    <xs:sequence>
      <xs:element name="Name" type="NameType">
        </xs:element>
      <xs:element name="Note" type="NoteType" minOccurs="0">
        </xs:element>
      <xs:element name="ExpirationDate" type="ExpirationDateType" minOccurs="0">
        </xs:element>
      <xs:element name="Specification" type="SpecificationType" minOccurs="0">
        </xs:element>
      <xs:element name="Quantity" type="QuantityType">
        </xs:element>
      <xs:element name="BatchOrSerialNumber" type="BatchOrSerialNumberType">
        </xs:element>
      <xs:element name="SealSeriesID" type="SealSeriesIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="ExpirationDateType">
    <xs:restriction base="xs:date"/>
  </xs:simpleType>

  <xs:simpleType name="SpecificationType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="BatchOrSerialNumberType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="B">
        </xs:enumeration>
      <xs:enumeration value="S">
        </xs:enumeration>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="SealSeriesIDType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="NonTaxedDepositsType">
    <xs:sequence>
      <xs:element name="NonTaxedDeposit" type="NonTaxedDepositType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="NonTaxedDepositType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
      <xs:element name="VariableSymbol" type="VariableSymbolType">
        </xs:element>
      <xs:element name="DepositAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="DepositAmount" type="AmountType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="VariableSymbolType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="TaxedDepositsType">
    <xs:sequence>
      <xs:element name="TaxedDeposit" type="TaxedDepositType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="TaxedDepositType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
      <xs:element name="VariableSymbol" type="VariableSymbolType">
        </xs:element>
      <xs:element name="TaxableDepositAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="TaxableDepositAmount" type="AmountType">
        </xs:element>
      <xs:element name="TaxInclusiveDepositAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="TaxInclusiveDepositAmount" type="AmountType">
        </xs:element>
      <xs:element name="ClassifiedTaxCategory" type="ClassifiedTaxCategoryType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="TaxTotalType">
    <xs:sequence>
      <xs:element name="TaxSubTotal" type="TaxSubTotalType" maxOccurs="unbounded">
        </xs:element>
      <xs:element name="TaxAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="TaxAmount" type="AmountType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="TaxSubTotalType">
    <xs:sequence>
      <xs:element name="TaxableAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="TaxableAmount" type="AmountType">
        </xs:element>
      <xs:element name="TaxAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="TaxAmount" type="AmountType">
        </xs:element>
      <xs:element name="TaxInclusiveAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="TaxInclusiveAmount" type="AmountType">
        </xs:element>
      <xs:element name="AlreadyClaimedTaxableAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="AlreadyClaimedTaxableAmount" type="AmountType">
        </xs:element>
      <xs:element name="AlreadyClaimedTaxAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="AlreadyClaimedTaxAmount" type="AmountType">
        </xs:element>
      <xs:element name="AlreadyClaimedTaxInclusiveAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="AlreadyClaimedTaxInclusiveAmount" type="AmountType">
        </xs:element>
      <xs:element name="DifferenceTaxableAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="DifferenceTaxableAmount" type="AmountType">
        </xs:element>
      <xs:element name="DifferenceTaxAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="DifferenceTaxAmount" type="AmountType">
        </xs:element>
      <xs:element name="DifferenceTaxInclusiveAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="DifferenceTaxInclusiveAmount" type="AmountType">
        </xs:element>
      <xs:element name="TaxCategory" type="TaxCategoryType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="TaxCategoryType">
    <xs:sequence>
      <xs:element name="Percent" type="PercentType">
        </xs:element>
      <xs:element name="TaxScheme" type="TaxSchemeType" minOccurs="0">
        </xs:element>
      <xs:element name="VATApplicable" type="VATApplicableType" minOccurs="0">
        </xs:element>
      <xs:element name="LocalReverseChargeFlag" type="BooleanType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="LegalMonetaryTotalType">
    <xs:sequence>
      <xs:element name="TaxExclusiveAmount" type="AmountType">
        </xs:element>
      <xs:element name="TaxExclusiveAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="TaxInclusiveAmount" type="AmountType">
        </xs:element>
      <xs:element name="TaxInclusiveAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="AlreadyClaimedTaxExclusiveAmount" type="AmountType">
        </xs:element>
      <xs:element name="AlreadyClaimedTaxExclusiveAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="AlreadyClaimedTaxInclusiveAmount" type="AmountType">
        </xs:element>
      <xs:element name="AlreadyClaimedTaxInclusiveAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="DifferenceTaxExclusiveAmount" type="AmountType">
        </xs:element>
      <xs:element name="DifferenceTaxExclusiveAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="DifferenceTaxInclusiveAmount" type="AmountType">
        </xs:element>
      <xs:element name="DifferenceTaxInclusiveAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="PayableRoundingAmount" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="PayableRoundingAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="PaidDepositsAmount" type="AmountType">
        </xs:element>
      <xs:element name="PaidDepositsAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
      <xs:element name="PayableAmount" type="AmountType">
        </xs:element>
      <xs:element name="PayableAmountCurr" type="AmountType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="PaymentMeansType">
    <xs:sequence>
      <xs:element name="Payment" type="PaymentType" maxOccurs="unbounded">
        </xs:element>
      <xs:element name="AlternateBankAccounts" type="AlternateBankAccountsType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="PaymentType">
    <xs:sequence>
      <xs:element name="PaidAmount" type="AmountType">
        </xs:element>
      <xs:element name="PaymentMeansCode" type="PaymentMeansCodeType">
        </xs:element>
      <xs:element name="Details" type="DetailsType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attribute name="partialPayment" type="BooleanType">
      </xs:attribute>
  </xs:complexType>

  <xs:simpleType name="PaymentMeansCodeType">
    <xs:restriction base="xs:integer">
      <xs:enumeration value="10">
        </xs:enumeration>
      <xs:enumeration value="20">
        </xs:enumeration>
      <xs:enumeration value="31">
        </xs:enumeration>
      <xs:enumeration value="42">
        </xs:enumeration>
      <xs:enumeration value="48">
        </xs:enumeration>
      <xs:enumeration value="49">
        </xs:enumeration>
      <xs:enumeration value="50">
        </xs:enumeration>
      <xs:enumeration value="97">
        </xs:enumeration>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="DetailsType">
    <xs:sequence>
      <xs:choice>
        <xs:sequence>
          <xs:element name="DocumentID" type="DocumentIDType">
            </xs:element>
          <xs:element name="IssueDate" type="IssueDateType">
            </xs:element>
        </xs:sequence>
        <xs:sequence>
          <xs:element name="PaymentDueDate" type="PaymentDueDateType">
            </xs:element>
          <xs:group ref="BankAccount"/>
          <xs:element name="VariableSymbol" type="VariableSymbolType" minOccurs="0">
            </xs:element>
          <xs:element name="ConstantSymbol" type="ConstantSymbolType" minOccurs="0">
            </xs:element>
          <xs:element name="SpecificSymbol" type="SpecificSymbolType" minOccurs="0">
            </xs:element>
        </xs:sequence>
      </xs:choice>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="DocumentIDType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="PaymentDueDateType">
    <xs:restriction base="xs:date"/>
  </xs:simpleType>

  <xs:simpleType name="BankCodeType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="IBANType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="BICType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="ConstantSymbolType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="SpecificSymbolType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="AlternateBankAccountsType">
    <xs:sequence>
      <xs:element name="AlternateBankAccount" type="AlternateBankAccountType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="AlternateBankAccountType">
    <xs:group ref="BankAccount"/>
  </xs:complexType>

  <xs:group name="BankAccount">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
      <xs:element name="BankCode" type="BankCodeType">
        </xs:element>
      <xs:element name="Name" type="NameType">
        </xs:element>
      <xs:element name="IBAN" type="IBANType">
        </xs:element>
      <xs:element name="BIC" type="BICType">
        </xs:element>
    </xs:sequence>
  </xs:group>

  <xs:attributeGroup name="RefAttribute">
    <xs:attribute name="ref" type="IDType" use="required">
      </xs:attribute>
  </xs:attributeGroup>

  <xs:attributeGroup name="IdAttribute">
    <xs:attribute name="id" type="IDType">
      </xs:attribute>
  </xs:attributeGroup>

  <xs:simpleType name="EgovFlagType">
    <xs:restriction base="BooleanType"/>
  </xs:simpleType>

  <xs:simpleType name="FileReferenceType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="ReferenceNumberType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="ISDS_IDType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="EgovClassifierType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="EgovClassifiersType">
    <xs:sequence>
      <xs:element name="EgovClassifier" type="EgovClassifierType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>
  
  <xs:element name="Invoice">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="DocumentType" type="DocumentTypeType">
          </xs:element>
        <xs:sequence minOccurs="0">
          <xs:element name="SubDocumentType" type="SubDocumentTypeType">
            </xs:element>
          <xs:element name="SubDocumentTypeOrigin" type="SubDocumentTypeOriginType">
            </xs:element>
        </xs:sequence>
        <xs:element name="TargetConsolidator" type="TargetConsolidatorType" minOccurs="0">
          </xs:element>
        <xs:element name="ClientOnTargetConsolidator" type="ClientOnTargetConsolidatorType" minOccurs="0">
          </xs:element>
        <xs:element name="ClientBankAccount" type="ClientBankAccountType" minOccurs="0">
          </xs:element>
        <xs:element name="ID" type="IDType">
          </xs:element>
        <xs:element name="UUID" type="UUIDType">
          </xs:element>
        <xs:element name="EgovFlag" type="EgovFlagType" minOccurs="0">
          </xs:element>
        <xs:element name="ISDS_ID" type="ISDS_IDType" minOccurs="0">
          </xs:element>
        <xs:element name="FileReference" type="FileReferenceType" minOccurs="0">
          </xs:element>
        <xs:element name="ReferenceNumber" type="ReferenceNumberType" minOccurs="0">
          </xs:element>
        <xs:element name="EgovClassifiers" type="EgovClassifiersType" minOccurs="0">
          </xs:element>
        <xs:element name="IssuingSystem" type="IssuingSystemType" minOccurs="0">
          </xs:element>
        <xs:element name="IssueDate" type="IssueDateType">
          </xs:element>
        <xs:element name="TaxPointDate" type="TaxPointDateType" minOccurs="0">
          </xs:element>
        <xs:element name="VATApplicable" type="VATApplicableType">
          </xs:element>
        <xs:element name="ElectronicPossibilityAgreementReference" type="NoteType">
          </xs:element>
        <xs:element name="Note" type="NoteType" minOccurs="0">
          </xs:element>
        <xs:element name="LocalCurrencyCode" type="CurrencyCodeType">
          </xs:element>
        <xs:element name="ForeignCurrencyCode" type="CurrencyCodeType" minOccurs="0">
          </xs:element>
        <xs:element name="CurrRate" type="CurrRateType">
          </xs:element>
        <xs:element name="RefCurrRate" type="RefCurrRateType">
          </xs:element>
        <xs:element name="Extensions" type="ExtensionsType" minOccurs="0">
          </xs:element>
        <xs:element name="AccountingSupplierParty" type="AccountingSupplierPartyType">
          </xs:element>
        <xs:element name="SellerSupplierParty" type="SellerSupplierPartyType" minOccurs="0">
          </xs:element>
        <xs:choice>
          <xs:element name="AccountingCustomerParty" type="AccountingCustomerPartyType">
            </xs:element>
          <xs:sequence>
            <xs:element name="AnonymousCustomerParty" type="AnonymousCustomerPartyType">
              </xs:element>
            <xs:element name="AccountingCustomerParty" type="AccountingCustomerPartyType" minOccurs="0">
              </xs:element>
          </xs:sequence>
        </xs:choice>
        <xs:element name="BuyerCustomerParty" type="BuyerCustomerPartyType" minOccurs="0">
          </xs:element>
        <xs:element name="OrderReferences" type="OrderReferencesType" minOccurs="0">
          </xs:element>
        <xs:element name="DeliveryNoteReferences" type="DeliveryNoteReferencesType" minOccurs="0">
          </xs:element>
        <xs:element name="OriginalDocumentReferences" type="OriginalDocumentReferencesType" minOccurs="0">
          </xs:element>
        <xs:element name="ContractReferences" type="ContractReferencesType" minOccurs="0">
          </xs:element>
        <xs:element name="Delivery" type="DeliveryType" minOccurs="0">
          </xs:element>
        <xs:element name="InvoiceLines" type="InvoiceLinesType">
          </xs:element>
        <xs:element name="NonTaxedDeposits" type="NonTaxedDepositsType" minOccurs="0">
          </xs:element>
        <xs:element name="TaxedDeposits" type="TaxedDepositsType" minOccurs="0">
          </xs:element>
        <xs:element name="TaxTotal" type="TaxTotalType">
          </xs:element>
        <xs:element name="LegalMonetaryTotal" type="LegalMonetaryTotalType">
          </xs:element>
        <xs:element name="PaymentMeans" type="PaymentMeansType" minOccurs="0">
          </xs:element>
        <xs:element name="SupplementsList" type="SupplementsListType" minOccurs="0">
          </xs:element>
        <xs:group ref="Signature" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="version" use="required" type="VersionType">
        </xs:attribute>
    </xs:complexType>
    <xs:unique name="OrderReferences">
      <xs:selector xpath="isdoc:OrderReferences/isdoc:OrderReference"/>
      <xs:field xpath="@id"/>
    </xs:unique>
    <xs:keyref name="OrderReferencesRef" refer="OrderReferences">
      <xs:selector xpath="isdoc:InvoiceLines/isdoc:InvoiceLine/isdoc:OrderReference"/>
      <xs:field xpath="@ref"/>
    </xs:keyref>
    <xs:unique name="DeliveryNoteReferences">
      <xs:selector xpath="isdoc:DeliveryNoteReferences/isdoc:DeliveryNoteReference"/>
      <xs:field xpath="@id"/>
    </xs:unique>
    <xs:keyref name="DeliveryNoteReferencesRef" refer="DeliveryNoteReferences">
      <xs:selector xpath="isdoc:InvoiceLines/isdoc:InvoiceLine/isdoc:DeliveryNoteReference"/>
      <xs:field xpath="@ref"/>
    </xs:keyref>
    <xs:unique name="OriginalDocumentReferences">
      <xs:selector xpath="isdoc:OriginalDocumentReferences/isdoc:OriginalDocumentReference"/>
      <xs:field xpath="@id"/>
    </xs:unique>
    <xs:keyref name="OriginalDocumentReferencesRef" refer="OriginalDocumentReferences">
      <xs:selector xpath="isdoc:InvoiceLines/isdoc:InvoiceLine/isdoc:OriginalDocumentReference"/>
      <xs:field xpath="@ref"/>
    </xs:keyref>    
    <xs:unique name="ContractReferences">
      <xs:selector xpath="isdoc:ContractReferences/isdoc:ContractReference"/>
      <xs:field xpath="@id"/>
    </xs:unique>
    <xs:keyref name="ContractReferencesRef" refer="ContractReferences">
      <xs:selector xpath="isdoc:InvoiceLines/isdoc:InvoiceLine/isdoc:ContractReference"/>
      <xs:field xpath="@ref"/>
    </xs:keyref>
    <xs:key name="InvoiceLines">
      <xs:selector xpath="isdoc:InvoiceLines/isdoc:InvoiceLine"/>
      <xs:field xpath="isdoc:ID"/>
    </xs:key>
  </xs:element>
  
</xs:schema>`
```

## File: `tests/index.ts`
```typescript
import { Invoice, InvoiceType, attachISDOC, extractISDOC, hasISDOC } from '..'
import { readFileSync, writeFileSync } from 'fs'
import { before } from 'mocha'
import { expect } from 'chai'
import createISDOCX from '../lib/createISDOCX'
import Zip from 'jszip'

const test0 = readFileSync(__dirname + '/test000.pdf'),
      test1 = readFileSync(__dirname + '/test001.isdoc.pdf'),
      test2 = readFileSync(__dirname + '/test002.isdoc.pdf'),
      invoice = readFileSync(__dirname + '/invoice.isdoc'),
      template = {
        DocumentType: 'invoice',
        ID: 1,
        IssuingSystem: 'ΔO Delta Zero',
        IssueDate: new Date(),
        TaxPointDate: new Date(),
        VATApplicable: true,
        AccountingSupplierParty: {
          Party: {
            PartyIdentification: {ID: '12345678'},
            PartyName: {Name: 'Test s.r.o.'},
            PostalAddress: {
              StreetName: 'Dodavatelská',
              BuildingNumber: '1',
              CityName: 'Dodavatelov',
              PostalZone: '12345',
              Country: {IdentificationCode: 'CZ', Name: ''}
            },
            PartyTaxScheme: {
              CompanyID: 'CZ12345678',
              TaxScheme: 'VAT'
            },
            Contact: {
              Telephone: '222111000',
              ElectronicMail: 'dodavatel@posta.cz'
            }
          }
        },
        AccountingCustomerParty: {
          Party: {
            PartyIdentification: {ID: '12345678'},
            PartyName: {Name: 'Test s.r.o.'},
            PostalAddress: {
              StreetName: 'Dodavatelská',
              BuildingNumber: '1',
              CityName: 'Dodavatelov',
              PostalZone: '12345',
              Country: {IdentificationCode: 'CZ', Name: ''}
            },
            PartyTaxScheme: {
              CompanyID: 'CZ12345678',
              TaxScheme: 'VAT'
            },
            Contact: {
              Telephone: '222111000',
              ElectronicMail: 'dodavatel@posta.cz'
            }
          }
        },
        InvoiceLines: {
          InvoiceLine: [
            {
              ID: '10001',
              InvoicedQuantity: 1,
              LineExtensionAmount: 100,
              LineExtensionAmountTaxInclusive: 121,
              LineExtensionTaxAmount: 21,
              UnitPrice: 100,
              UnitPriceTaxInclusive: 121,
              ClassifiedTaxCategory: {Percent: 21, VATCalculationMethod: 0, VATApplicable: true},
              Item: {Description: 'Zboží 10001'}
            },
          ]
        },
        TaxTotal: {
          TaxSubTotal: {
            TaxableAmount: 100,
            TaxAmount: 21,
            TaxInclusiveAmount: 121,
            AlreadyClaimedTaxableAmount: 0,
            AlreadyClaimedTaxAmount: 0,
            AlreadyClaimedTaxInclusiveAmount: 0,
            DifferenceTaxableAmount: 100,
            DifferenceTaxAmount: 21,
            DifferenceTaxInclusiveAmount: 121,
            TaxCategory: {
              Percent: 21,
              VATApplicable: true,
            }
          },
          TaxAmount: 21
        },
        LegalMonetaryTotal: {
          TaxExclusiveAmount: 5500,
          TaxInclusiveAmount: 6655,
          AlreadyClaimedTaxExclusiveAmount: 0,
          AlreadyClaimedTaxInclusiveAmount: 0,
          DifferenceTaxExclusiveAmount: 5500,
          DifferenceTaxInclusiveAmount: 6655,
          PayableRoundingAmount: 0,
          PaidDepositsAmount: 0,
          PayableAmount: 6655
        },
        PaymentMeans: {
          Payment: {
            PaidAmount: 6655,
            PaymentMeansCode: 42,
            Details: {
              PaymentDueDate: new Date(),
              ID: 1234567890,
              BankCode: 1234,
              Name: 'BANKA',
              IBAN: '',
              BIC: '',
              VariableSymbol: 10111,
              ConstantSymbol: '',
              SpecificSymbol: ''
            }
          }
        }
      }

describe('Extracting ISDOCs', () => {
  it ('test000.pdf -> false', async () => {
    expect(await hasISDOC(test0)).to.be.false
  })

  it ('test001.isdoc.pdf -> true', async () => {
    expect(await hasISDOC(test1)).to.be.true
    const isdoc = await extractISDOC(test1)
    expect(isdoc).to.be.instanceof(Invoice)
    expect(isdoc?.ID).to.be.eq('FV-1/2021')
    expect(isdoc?.UUID).to.be.eq('AEC4791C-4BA1-451E-A1DC-2BF634B1C29D')
    expect(isdoc?.['$_version']).to.be.eq('6.0.2')
  })

  it ('test002.isdoc.pdf -> true', async () => {
    expect(await hasISDOC(test2)).to.be.true
    const isdoc = await extractISDOC(test2)
    expect(isdoc).to.be.instanceof(Invoice)
    expect(isdoc?.ID).to.be.eq('FV-2/2021')
    expect(isdoc?.UUID).to.be.eq('A34D00BF-FFB3-445B-BA1F-C5764B89409E')
    expect(isdoc?.['$_version']).to.be.eq('6.0.2')
  })
})

describe('Attaching ISDOC', () => {
  it ('test000.pdf -> test000.isdoc.pdf', async () => {
    const test0isdoc = await attachISDOC(test0, template as InvoiceType)
    expect(test0isdoc).to.be.instanceof(Buffer)
    writeFileSync(__dirname + '/test000.isdoc.pdf', test0isdoc)
  })

  it ('test000.isdoc.pdf is valid', async () => {
    const test0i = readFileSync(__dirname + '/test000.isdoc.pdf')
    expect(await hasISDOC(test0i)).to.be.true

    const isdoc = await extractISDOC(test0i)
    expect(isdoc).to.be.instanceof(Invoice)
    expect(isdoc?.ID?.toString()).to.be.eq('1')
    expect(isdoc?.UUID).to.be.match(/[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}/)
    expect(isdoc?.['$_version']).to.be.eq('6.0.1')
  })

  it ('test001.isdoc.pdf -> throws that it already has one', async () => {
    expect(await attachISDOC(test1, invoice).catch(e => e.message)).to.be.include('This PDF Already Has an ISDOC Attachment')
  })
})

describe('Creating ISDOCX archive', () => {
  it ('test000.pdf + invoice.isdoc -> test000.isdox', async () => {
    const isdocx = await createISDOCX(test0, invoice)
    expect(isdocx).to.be.instanceof(Buffer)
    writeFileSync(__dirname + '/test000.isdocx', isdocx)
  })

  it ('test001.isdoc.pdf + invoice.isdoc -> throws ', async () => {
    expect(await createISDOCX(test1, invoice).catch(e => e.message)).to.be.include('This PDF Already Has an ISDOC Attachment')
  })
})

describe('Validating created ISDOCX archive', () => {
  let zip : Zip

  before(async () => {
    zip = await new Zip().loadAsync(readFileSync(__dirname + '/test000.isdocx'))
  })

  it ('test000.isdox is readable', async () => {
    expect(zip.files).to.be.an('object')
    expect(Object.keys(zip.files)).to.be.an('Array')
  })

  it ('test000.isdox has 3 files', async () => {
    expect(Object.keys(zip.files).length).to.be.eq(3)
  })

  it ('test000.isdox has a .pdf', async () => {
    expect(Object.keys(zip.files).find(r => r.match(/\.pdf$/i))).to.be.a('string')
  })

  it ('test000.isdox has a .isdoc', async () => {
    expect(Object.keys(zip.files).find(r => r.match(/\.isdoc$/i))).to.be.a('string')
  })

  it ('test000.isdox has a valid .isdoc', async () => {
    const name = Object.keys(zip.files).find(r => r.match(/\.isdoc$/i)) as string,
          file = await zip.file(name)?.async('nodebuffer'),
          isdoc = new Invoice(file)
    expect(isdoc?.['$_version']).to.be.eq('6.0.1')
  })

  it ('test000.isdox has a manifest.xml', async () => {
    expect(Object.keys(zip.files).find(r => r.toLowerCase() === 'manifest.xml')).to.be.a('string')
  })
})

// describe('Clean Up', () => {
//   it ('Clean Up', () => {
//     expect((() => {
//       rmSync(__dirname + '/test000.isdoc.pdf')
//       rmSync(__dirname + '/test000.isdocx')
//       return true
//     })()).not.to.throw
//   })
// })
```

## File: `tests/invoice.isdoc`
```
<?xml version="1.0" encoding="utf-8" ?> 
<Invoice xmlns="http://isdoc.cz/namespace/2013" version="6.0.1">
<DocumentType>1</DocumentType>
<TargetConsolidator></TargetConsolidator>
<ClientOnTargetConsolidator></ClientOnTargetConsolidator>
<ID>FV-1/2021</ID>
<UUID>AEC4791C-4BA1-451E-A1DC-2BF634B1C29D</UUID>
<IssuingSystem>ABRA Gen® 21.1.4</IssuingSystem>
<IssueDate>2021-04-01</IssueDate>
<TaxPointDate>2021-04-01</TaxPointDate>
<VATApplicable>true</VATApplicable>
<ElectronicPossibilityAgreementReference></ElectronicPossibilityAgreementReference>
<Note></Note>
<LocalCurrencyCode>CZK</LocalCurrencyCode>
<CurrRate>1</CurrRate>
<RefCurrRate>1</RefCurrRate>
<AccountingSupplierParty><Party><PartyIdentification><UserID></UserID>
<CatalogFirmIdentification>0</CatalogFirmIdentification>
<ID>12345678</ID>
</PartyIdentification>
<PartyName><Name>Demoverze</Name>
</PartyName>
<PostalAddress><StreetName>Dodavatelská</StreetName>
<BuildingNumber>1</BuildingNumber>
<CityName>Dodavatelov</CityName>
<PostalZone>12345</PostalZone>
<Country><IdentificationCode>CZ</IdentificationCode>
<Name></Name>
</Country>
</PostalAddress>
<PartyTaxScheme><CompanyID>CZ12345678</CompanyID>
<TaxScheme>VAT</TaxScheme>
</PartyTaxScheme>
<Contact><Telephone>123123123</Telephone>
<ElectronicMail>dodavatel@posta.cz</ElectronicMail>
</Contact>
</Party>
</AccountingSupplierParty>
<AccountingCustomerParty><Party><PartyIdentification><UserID>000001</UserID>
<CatalogFirmIdentification>0</CatalogFirmIdentification>
<ID>11122233</ID>
</PartyIdentification>
<PartyName><Name>Odběratel 1</Name>
</PartyName>
<PostalAddress><StreetName>Udběratelská</StreetName>
<BuildingNumber>123</BuildingNumber>
<CityName>Odběratelův Dvůr</CityName>
<PostalZone>12345</PostalZone>
<Country><IdentificationCode>CZ</IdentificationCode><Name></Name>
</Country></PostalAddress>
<PartyTaxScheme><CompanyID>CZ11122233</CompanyID>
<TaxScheme>VAT</TaxScheme>
</PartyTaxScheme>
<Contact><Name></Name>
<Telephone></Telephone>
<ElectronicMail></ElectronicMail>
</Contact>
</Party>
</AccountingCustomerParty>
<DeliveryNoteReferences><DeliveryNoteReference id="DL-1/2021">
<ID>DL-1/2021</ID>
<IssueDate>2021-04-01</IssueDate>
</DeliveryNoteReference>
</DeliveryNoteReferences><InvoiceLines><InvoiceLine><ID>1000000101</ID>
<InvoicedQuantity unitCode="">0</InvoicedQuantity>
<LineExtensionAmount>0</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>0</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>0</LineExtensionTaxAmount>
<UnitPrice>0</UnitPrice>
<UnitPriceTaxInclusive>0</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>0</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Fakturace zboží</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID></ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID></ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>5000000101</ID>
<DeliveryNoteReference ref="DL-1/2021"><LineID>1010000101</LineID>
</DeliveryNoteReference>
<InvoicedQuantity unitCode="ks">1</InvoicedQuantity>
<LineExtensionAmount>100</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>121</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>21</LineExtensionTaxAmount>
<UnitPrice>100</UnitPrice>
<UnitPriceTaxInclusive>121</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>21</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zboží 1</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID>000001</ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID>001-001</ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>6000000101</ID>
<DeliveryNoteReference ref="DL-1/2021"><LineID>2010000101</LineID>
</DeliveryNoteReference>
<InvoicedQuantity unitCode="ks">1</InvoicedQuantity>
<LineExtensionAmount>200</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>242</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>42</LineExtensionTaxAmount>
<UnitPrice>200</UnitPrice>
<UnitPriceTaxInclusive>242</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>21</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zboží 2</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID>000002</ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID>001-002</ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>7000000101</ID>
<DeliveryNoteReference ref="DL-1/2021"><LineID>3010000101</LineID>
</DeliveryNoteReference>
<InvoicedQuantity unitCode="ks">1</InvoicedQuantity>
<LineExtensionAmount>300</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>363</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>63</LineExtensionTaxAmount>
<UnitPrice>300</UnitPrice>
<UnitPriceTaxInclusive>363</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>21</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zboží 3</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID>000003</ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID>001-003</ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>8000000101</ID>
<DeliveryNoteReference ref="DL-1/2021"><LineID>4010000101</LineID>
</DeliveryNoteReference>
<InvoicedQuantity unitCode="ks">1</InvoicedQuantity>
<LineExtensionAmount>400</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>484</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>84</LineExtensionTaxAmount>
<UnitPrice>400</UnitPrice>
<UnitPriceTaxInclusive>484</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>21</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zboží 4</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID>000004</ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID>001-004</ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>9000000101</ID>
<DeliveryNoteReference ref="DL-1/2021"><LineID>5010000101</LineID>
</DeliveryNoteReference>
<InvoicedQuantity unitCode="ks">1</InvoicedQuantity>
<LineExtensionAmount>500</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>605</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>105</LineExtensionTaxAmount>
<UnitPrice>500</UnitPrice>
<UnitPriceTaxInclusive>605</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>21</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zboží 5</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID>000005</ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID>001-005</ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>A000000101</ID>
<DeliveryNoteReference ref="DL-1/2021"><LineID>6010000101</LineID>
</DeliveryNoteReference>
<InvoicedQuantity unitCode="ks">1</InvoicedQuantity>
<LineExtensionAmount>600</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>726</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>126</LineExtensionTaxAmount>
<UnitPrice>600</UnitPrice>
<UnitPriceTaxInclusive>726</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>21</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zboží 6</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID>000006</ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID>001-006</ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>B000000101</ID>
<DeliveryNoteReference ref="DL-1/2021"><LineID>7010000101</LineID>
</DeliveryNoteReference>
<InvoicedQuantity unitCode="ks">1</InvoicedQuantity>
<LineExtensionAmount>700</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>847</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>147</LineExtensionTaxAmount>
<UnitPrice>700</UnitPrice>
<UnitPriceTaxInclusive>847</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>21</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zboží 7</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID>000007</ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID>001-007</ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>C000000101</ID>
<DeliveryNoteReference ref="DL-1/2021"><LineID>8010000101</LineID>
</DeliveryNoteReference>
<InvoicedQuantity unitCode="ks">1</InvoicedQuantity>
<LineExtensionAmount>800</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>968</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>168</LineExtensionTaxAmount>
<UnitPrice>800</UnitPrice>
<UnitPriceTaxInclusive>968</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>21</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zboží 8</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID>000008</ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID>001-008</ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>D000000101</ID>
<DeliveryNoteReference ref="DL-1/2021"><LineID>9010000101</LineID>
</DeliveryNoteReference>
<InvoicedQuantity unitCode="ks">1</InvoicedQuantity>
<LineExtensionAmount>900</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>1089</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>189</LineExtensionTaxAmount>
<UnitPrice>900</UnitPrice>
<UnitPriceTaxInclusive>1089</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>21</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zboží 9</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID>000009</ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID>001-009</ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>E000000101</ID>
<DeliveryNoteReference ref="DL-1/2021"><LineID>A010000101</LineID>
</DeliveryNoteReference>
<InvoicedQuantity unitCode="ks">1</InvoicedQuantity>
<LineExtensionAmount>1000</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>1210</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>210</LineExtensionTaxAmount>
<UnitPrice>1000</UnitPrice>
<UnitPriceTaxInclusive>1210</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>21</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zboží 10</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID>000010</ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID>001-010</ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>4000000101</ID>
<InvoicedQuantity unitCode="">0</InvoicedQuantity>
<LineExtensionAmount>0</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>0</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>0</LineExtensionTaxAmount>
<UnitPrice>0</UnitPrice>
<UnitPriceTaxInclusive>0</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>0</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zaokrouhlení nezahrnuté do základu daně</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID></ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID></ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
<InvoiceLine><ID>2000000101</ID>
<InvoicedQuantity unitCode="">0</InvoicedQuantity>
<LineExtensionAmount>0</LineExtensionAmount>
<LineExtensionAmountTaxInclusive>0</LineExtensionAmountTaxInclusive>
<LineExtensionTaxAmount>0</LineExtensionTaxAmount>
<UnitPrice>0</UnitPrice>
<UnitPriceTaxInclusive>0</UnitPriceTaxInclusive>
<ClassifiedTaxCategory><Percent>21</Percent>
<VATCalculationMethod>0</VATCalculationMethod>
<VATApplicable>true</VATApplicable>
</ClassifiedTaxCategory>
<Note></Note>
<VATNote></VATNote>
<Item><Description>Zaokrouhlení pro sazbu DPH</Description>
<CatalogueItemIdentification><ID></ID>
</CatalogueItemIdentification>
<SellersItemIdentification><ID></ID>
</SellersItemIdentification>
<SecondarySellersItemIdentification><ID></ID>
</SecondarySellersItemIdentification>
<TertiarySellersItemIdentification><ID></ID>
</TertiarySellersItemIdentification>
<BuyersItemIdentification><ID></ID>
</BuyersItemIdentification>
</Item>
</InvoiceLine>
</InvoiceLines><TaxTotal><TaxSubTotal><TaxableAmount>5500</TaxableAmount>
<TaxAmount>1155</TaxAmount>
<TaxInclusiveAmount>6655</TaxInclusiveAmount>
<AlreadyClaimedTaxableAmount>0</AlreadyClaimedTaxableAmount>
<AlreadyClaimedTaxAmount>0</AlreadyClaimedTaxAmount>
<AlreadyClaimedTaxInclusiveAmount>0</AlreadyClaimedTaxInclusiveAmount>
<DifferenceTaxableAmount>5500</DifferenceTaxableAmount><DifferenceTaxAmount>1155</DifferenceTaxAmount>
<DifferenceTaxInclusiveAmount>6655</DifferenceTaxInclusiveAmount>
<TaxCategory><Percent>21</Percent>
<VATApplicable>true</VATApplicable>
<LocalReverseChargeFlag>false</LocalReverseChargeFlag>
</TaxCategory>
</TaxSubTotal>
<TaxAmount>1155</TaxAmount>
</TaxTotal>
<LegalMonetaryTotal><TaxExclusiveAmount>5500</TaxExclusiveAmount>
<TaxInclusiveAmount>6655</TaxInclusiveAmount>
<AlreadyClaimedTaxExclusiveAmount>0</AlreadyClaimedTaxExclusiveAmount>
<AlreadyClaimedTaxInclusiveAmount>0</AlreadyClaimedTaxInclusiveAmount>
<DifferenceTaxExclusiveAmount>5500</DifferenceTaxExclusiveAmount>
<DifferenceTaxInclusiveAmount>6655</DifferenceTaxInclusiveAmount>
<PayableRoundingAmount>0</PayableRoundingAmount>
<PaidDepositsAmount>0</PaidDepositsAmount>
<PayableAmount>6655</PayableAmount>
</LegalMonetaryTotal>
<PaymentMeans><Payment><PaidAmount>6655</PaidAmount>
<PaymentMeansCode>42</PaymentMeansCode>
<Details><PaymentDueDate>2021-04-15</PaymentDueDate>
<ID>1234567890</ID>
<BankCode>1234</BankCode>
<Name>BANKA</Name>
<IBAN></IBAN>
<BIC></BIC>
<VariableSymbol>10111</VariableSymbol>
<ConstantSymbol></ConstantSymbol>
<SpecificSymbol></SpecificSymbol>
</Details>
</Payment>
</PaymentMeans>
</Invoice>
```


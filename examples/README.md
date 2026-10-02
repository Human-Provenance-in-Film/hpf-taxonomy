# Example records

Test records for [schema.json](../schema.json). They are fixtures for the
repository checks, not guidance. [taxonomy.md](../taxonomy.md) defines the
classifications and [INTEGRATION.md](../INTEGRATION.md) covers implementation.

`tools/check_standard.py` reads every `.json` file here. A file whose name
begins with `valid-` must validate against the schema. A file whose name
begins with `invalid-` must fail. Checking both directions matters: a change
that quietly widened the schema would still let the valid records pass, and
only the invalid ones would catch it.

Every record is made under the current version, 0.9.3, except the one marked
historical. Each invalid record breaks one rule only.

| File | What it covers |
| --- | --- |
| `valid-no-ai.json` | The minimum 0.9.3 record: the standard version, the released version and the classification. |
| `valid-assistive-ai.json` | Assistive AI with no descriptors. |
| `valid-assistive-ai-altered-performance.json` | Altered performance, the one descriptor that may appear on Assistive AI. |
| `valid-generative-ai-no-descriptors.json` | Descriptors are optional on Generative AI. |
| `valid-generative-ai-with-descriptors.json` | Two descriptors on a Generative AI record. |
| `valid-generative-ai-combined-performance-descriptors.json` | Digital replica, Generated voice and Altered performance together. Each records a different fact. |
| `valid-historical-0.9.2-record.json` | A record made under 0.9.2. It has no released-version field, which 0.9.2 did not define, and stays valid under the version it names. |
| `invalid-classification-outside-enum.json` | A classification value HPF does not define. |
| `invalid-missing-standard-version.json` | The version field is required, so a classification alone is not a record. |
| `invalid-standard-version-format.json` | The version field takes `MAJOR.MINOR` or `MAJOR.MINOR.PATCH`, with no prefix. |
| `invalid-missing-released-version.json` | A 0.9.3 record must identify the released version it covers. |
| `invalid-empty-released-version.json` | An empty released version identifies nothing. |
| `invalid-descriptors-on-assistive.json` | A descriptor other than Altered performance on an Assistive AI record. |
| `invalid-descriptor-outside-enum.json` | A descriptor value the schema does not list. |
| `invalid-empty-descriptors.json` | An empty array. Omit the field instead. |

## Adding a record

Name it for the case it covers, prefixed `valid-` or `invalid-`, and add a row
to the table above. Run `python3 tools/check_standard.py` before committing.

There is no record here for a production with no declaration, because there is
no such record. Where no HPF declaration exists, omit the record entirely. An
absent record and No AI Used are different states.

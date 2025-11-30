# Guidelines - Lista Pól (Fields List View)

## Podstawowe Informacje
Dokument zawiera wytyczne projektowe dla widoku tabelarycznego "Lista Pól" w systemie AMODIT. Bazuje na implementacji zakładki "Formularz" z funkcjonalnością konfiguracji pól, tłumaczeń i filtrowania.

---

## 1. Branding i Kolorystyka

### Kolory Podstawowe
- **Pomarańczowy (Primary)**: `#f97316` / `bg-orange-500` - główny kolor akcji, buttony, zaznaczenia
- **Pomarańczowy Hover**: `#ea580c` / `bg-orange-600`
- **Pomarańczowy Jasny**: `#fed7aa` / `bg-orange-50` - tło dla zaznaczonych elementów

### Kolory Funkcjonalne
- **Niebieski (Tłumaczenia)**: `bg-blue-50`, `border-blue-300`, `text-blue-700` - kolumny z tłumaczeniami
- **Szary (Tło)**: 
  - `bg-gray-50` - naprzemienne wiersze, nagłówki sekcji
  - `bg-gray-100` - hover state
  - `bg-gray-200` - nieaktywne elementy
- **Biały**: `bg-white` - główne tło tabeli

### Granice i Obramowania
- **Border Standard**: `border-gray-200` - 1px solid
- **Border Tłumaczeń**: `border-l-2 border-l-blue-300` - lewa krawędź kolumn tłumaczeń (2px)
- **Border Radius**: `rounded-lg` (8px) dla kontenerów głównych

---

## 2. Typografia i Rozmiary

### Rozmiary Czcionek (Wszystkie 14px zgodnie z guidelines)
```css
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 14px - domyślna */
```

### Font Weights
- **Normal**: `font-weight: 400` - tekst standardowy
- **Medium**: `font-weight: 500` - nagłówki, etykiety, przyciski

### Font Family
- **Mono**: `font-mono` - nazwy systemowe/techniczne
- **Sans**: domyślna - reszta interfejsu

### Wysokości Komponentów
- **Input/Button (Standard)**: `h-8` (32px)
- **Input (Kompaktowy)**: `h-7` (28px)
- **Icon Button**: `h-5 w-5` (20px)
- **Mini Icon Button**: `h-3.5 w-3.5` (14px)

---

## 3. Układ Tabeli

### Struktura Hierarchii
```
Sekcja (Section)
├── Pola bezpośrednie (Fields)
└── Tabele (Tables)
    └── Sekcje Tabeli (Table Sections)
        └── Pola w sekcji tabeli (Fields)
```

### Kolumny Główne (w kolejności)
1. **Nazwa systemowa** - sticky left, 220px, cień z prawej strony
2. **Typ** - 130px min-width
3. **Nazwa** - 180px min-width, rozszerzalna o tłumaczenia
4. **Podpowiedź** - 130px min-width, rozszerzalna o tłumaczenia
5. **Wartość domyślna** - 130px min-width
6. **Kolumna w bazie** - 130px min-width (domyślnie ukryta)

### Kolumny Rozszerzalne (Tłumaczenia)
Każda kolumna "Nazwa" i "Podpowiedź" może być rozwinięta do 4 kolumn:
- **Domyślna/PL** - zależnie od wybranego języka
- **EN** - angielska
- **DE** - niemiecka

**Logika wyświetlania tłumaczeń:**
- Gdy `viewLanguage === 'default'`: główna kolumna to "Domyślna", rozwinięcie pokazuje PL, EN, DE
- Gdy `viewLanguage === 'PL'`: główna kolumna to PL, rozwinięcie pokazuje Domyślna, EN, DE
- Gdy `viewLanguage === 'EN'`: główna kolumna to EN, rozwinięcie pokazuje Domyślna, PL, DE
- Gdy `viewLanguage === 'DE'`: główna kolumna to DE, rozwinięcie pokazuje Domyślna, PL, EN

### Sticky Column (Nazwa systemowa)
```tsx
className="sticky left-0 z-10 bg-white relative 
  after:absolute after:top-0 after:right-0 after:w-px after:h-full 
  after:shadow-[2px_0_4px_rgba(0,0,0,0.1)] after:pointer-events-none 
  w-[220px] min-w-[220px] max-w-[220px]"
```

### Wcięcia Hierarchiczne (Padding Left)
- **Sekcja główna**: 0px
- **Pole w sekcji**: 20px
- **Tabela**: 20px
- **Sekcja tabeli**: 40px
- **Pole w sekcji tabeli**: 60px

**Wzór**: `paddingLeft = level * 20px`

---

## 4. Typy Pól i Ikony

### Typy Pól (FieldType)
```typescript
type FieldType = 
  | 'data'         // Calendar icon
  | 'data-czas'    // Clock icon
  | 'tekstowe'     // Type icon
  | 'długi-tekst'  // AlignLeft icon
  | 'kwota'        // DollarSign icon
  | 'odnośnik'     // Link icon
  | 'słownik'      // BookOpen icon
  | 'lista';       // List icon
```

### Mapowanie Ikon (lucide-react)
```typescript
const fieldTypeIcons: Record<FieldType, React.ComponentType<any>> = {
  'data': Calendar,
  'data-czas': Clock,
  'tekstowe': Type,
  'długi-tekst': AlignLeft,
  'kwota': DollarSign,
  'odnośnik': Link,
  'słownik': BookOpen,
  'lista': List
};
```

### Etykiety Typów
```typescript
const fieldTypeLabels: Record<FieldType, string> = {
  'data': 'Data',
  'data-czas': 'Data i czas',
  'tekstowe': 'Tekstowe',
  'długi-tekst': 'Długi tekst',
  'kwota': 'Kwota',
  'odnośnik': 'Odnośnik',
  'słownik': 'Słownik',
  'lista': 'Lista'
};
```

---

## 5. System Edycji Inline

### Komponenty Edytowalne

#### EditableText Component
**Props:**
```typescript
interface EditableTextProps {
  value: string;
  onSave: (newValue: string) => void;
  placeholder?: string;
  emptyText?: string;
  className?: string;
  truncate?: boolean;        // Obcina długie teksty do 30 znaków
  asTag?: boolean;          // Renderuje jako klikany tag (nazwy systemowe)
  editingId: string;
  currentEditingId: string | null;
  onEditStart: (id: string) => void;
  onEditEnd: () => void;
  isInherited?: boolean;     // Dla dziedziczonych wartości
  inheritedValue?: string;   // Wartość dziedziczona
}
```

**Zachowanie:**
- **Kliknięcie**: Wejście w tryb edycji
- **Enter**: Zapisz i wyjdź
- **Escape**: Anuluj i wyjdź
- **Blur**: Automatyczny zapis
- **Podwójne kliknięcie** (dla asTag): Wejście w tryb edycji
- **Pojedyncze kliknięcie** (dla asTag): Kopiowanie do schowka

### Nazwy Systemowe (Technical Names)

**Wyświetlanie:**
```tsx
<div className="flex items-center gap-2 group">
  <span className="font-mono text-gray-600">{technicalName}</span>
  <div className="opacity-0 group-hover:opacity-100 transition-opacity">
    <Button>
      <Copy className="h-3 w-3" />
    </Button>
    <Button>
      <Edit2 className="h-3 w-3" />
    </Button>
  </div>
</div>
```

**Cechy:**
- Font mono
- Hover pokazuje ikony Copy i Edit
- Copy działa na kliknięcie
- Edit otwiera inline edytor

### Dziedziczenie Wartości (Tłumaczenia)

**Logika:**
- Puste pole w tłumaczeniu (np. EN) → wyświetla wartość z domyślnej (szarym kolorem)
- Wartość dziedziczona ma klasę `text-gray-500`
- Pusty placeholder to wartość domyślna

**Przykład:**
```tsx
isInherited={!field.displayNameEn}
inheritedValue={field.displayName || field.name}
```

---

## 6. System Filtrowania

### State Filtrów
```typescript
const [showFilters, setShowFilters] = useState(false);
const [fieldTypeFilters, setFieldTypeFilters] = useState<Set<FieldType>>(new Set());
```

### UI Filtrów

**Przycisk:**
```tsx
<Button variant="ghost" size="sm" className="h-8 w-8 p-0">
  <Filter className={hasActiveFilters() ? 'text-orange-600' : 'text-gray-600'} />
</Button>
```

**Popover z filtrami:**
```tsx
<PopoverContent className="w-64 p-0" align="end">
  {/* Nagłówek z przyciskiem "Wyczyść filtry" */}
  <div className="p-3 border-b">
    <div className="flex items-center justify-between">
      <span className="text-sm font-medium">Filtruj po typie pola</span>
      {hasActiveFilters() && (
        <Button onClick={clearAllFilters} 
          className="border-orange-500 text-orange-600">
          Wyczyść filtry
        </Button>
      )}
    </div>
  </div>
  
  {/* Lista checkboxów */}
  <div className="p-3 space-y-2">
    {getAllFieldTypes().map((fieldType) => (
      <div className="flex items-center space-x-2">
        <Checkbox checked={fieldTypeFilters.has(fieldType)} />
        <label>{fieldTypeLabels[fieldType]}</label>
      </div>
    ))}
  </div>
</PopoverContent>
```

### Logika Filtrowania

**Funkcje pomocnicze:**
```typescript
// Sprawdź czy pole pasuje do filtrów
const fieldMatchesFilters = (field: Field): boolean => {
  if (fieldTypeFilters.size === 0) return true;
  return fieldTypeFilters.has(field.fieldType || 'tekstowe');
};

// Pobierz wszystkie unikalne typy pól
const getAllFieldTypes = (): FieldType[] => {
  const fieldTypes = new Set<FieldType>();
  // Iteruj przez sections → fields
  // Iteruj przez sections → tables → fields
  // Iteruj przez sections → tables → sections → fields
  return Array.from(fieldTypes).sort();
};

// Sprawdź czy są aktywne filtry
const hasActiveFilters = () => fieldTypeFilters.size > 0;
```

**Filtrowanie sekcji:**
```typescript
const getFilteredSections = (): Section[] => {
  if (!hasActiveFilters()) return sections;
  
  return sections.map(section => {
    const filteredFields = section.fields.filter(fieldMatchesFilters);
    const filteredTables = section.tables.map(table => {
      const filteredTableFields = table.fields.filter(fieldMatchesFilters);
      const filteredTableSections = table.sections.map(tableSection => {
        const filteredSectionFields = tableSection.fields.filter(fieldMatchesFilters);
        return { ...tableSection, fields: filteredSectionFields };
      }).filter(ts => ts.fields.length > 0);
      
      return { ...table, fields: filteredTableFields, sections: filteredTableSections };
    }).filter(t => t.fields.length > 0 || t.sections.length > 0);
    
    return { ...section, fields: filteredFields, tables: filteredTables };
  }).filter(s => s.fields.length > 0 || s.tables.length > 0);
};
```

### Pusty Stan (Brak wyników)
```tsx
{getFilteredSections().length === 0 && hasActiveFilters() && (
  <div className="border rounded-lg p-8 text-center">
    <div className="flex flex-col items-center gap-3">
      <Filter className="h-8 w-8 text-gray-400" />
      <div>
        <h3 className="text-sm font-medium mb-1">Brak wyników</h3>
        <p className="text-sm text-gray-500 mb-3">
          Nie znaleziono pól spełniających wybrane kryteria filtrowania.
        </p>
        <Button onClick={clearAllFilters} 
          className="border-orange-500 text-orange-600">
          Wyczyść filtry
        </Button>
      </div>
    </div>
  </div>
)}
```

---

## 7. System Widoczności Kolumn

### State Widoczności
```typescript
const [showColumnConfig, setShowColumnConfig] = useState(false);
const [visibleColumns, setVisibleColumns] = useState({
  systemName: true,     // Nie można ukryć
  name: true,
  type: true,           // Nie można ukryć
  tooltip: true,
  defaultValue: true,
  columnName: false     // Domyślnie ukryta
});
```

### UI Konfiguracji Kolumn

**Przycisk:**
```tsx
<Button variant="ghost" size="sm" className="h-8 w-8 p-0">
  <Columns className="h-4 w-4 text-gray-600" />
</Button>
```

**Popover:**
```tsx
<PopoverContent className="w-64 p-0" align="end">
  <div className="p-3 border-b">
    <span className="text-sm font-medium">Widoczne kolumny</span>
  </div>
  <div className="p-3 space-y-3">
    <div className="flex items-center space-x-2">
      <Checkbox 
        checked={visibleColumns.systemName}
        disabled={true}
        className="opacity-50"
      />
      <label className="text-gray-500">Nazwa systemowa</label>
    </div>
    {/* Pozostałe checkboxy... */}
  </div>
</PopoverContent>
```

### Warunkowe Renderowanie Kolumn
```tsx
{/* W nagłówku tabeli */}
{visibleColumns.name && (
  <th className="border p-2">Nazwa</th>
)}

{/* W wierszu */}
{visibleColumns.name && (
  <td className="border p-1.5">
    <EditableText value={name} {...props} />
  </td>
)}
```

---

## 8. System Tłumaczeń

### Selector Języka (viewLanguage)
```tsx
<Select value={viewLanguage} onValueChange={setViewLanguage}>
  <SelectTrigger className="w-32">
    <SelectValue />
  </SelectTrigger>
  <SelectContent>
    <SelectItem value="default">Domyślne</SelectItem>
    <SelectItem value="PL">PL</SelectItem>
    <SelectItem value="EN">EN</SelectItem>
    <SelectItem value="DE">DE</SelectItem>
  </SelectContent>
</Select>
```

### Helper Function - Pobieranie Nazwy
```typescript
const getDisplayName = (): string => {
  switch (viewLanguage) {
    case 'EN':
      return field.displayNameEn || field.displayName || field.name;
    case 'DE':
      return field.displayNameDe || field.displayName || field.name;
    case 'PL':
    case 'default':
    default:
      return field.displayName || field.name;
  }
};
```

### Przycisk Rozwijania Tłumaczeń
```tsx
<Button
  variant="ghost"
  size="sm"
  onClick={() => toggleColumnExpansion('name')}
  className="h-5 w-5 p-0"
  title="Rozwiń tłumaczenia"
>
  <Languages className="h-3.5 w-3.5" />
</Button>
```

### Kolumny Tłumaczeń

**Styling:**
```tsx
className="border border-gray-200 p-1.5 bg-blue-50 border-l-2 border-l-blue-300"
```

**Nagłówki:**
```tsx
<th className="bg-blue-50 border-l-2 border-l-blue-300">
  <span className="text-sm text-blue-700">EN</span>
</th>
```

---

## 9. Interakcje i Stany

### Hover States
```css
/* Wiersz tabeli */
.hover:bg-gray-50

/* Grupa elementów */
.group-hover:opacity-100  /* Pokazuj ikony akcji */

/* Nazwa systemowa */
.group-hover/system-name:opacity-100

/* Typ pola */
.group-hover/field-type:opacity-100
```

### Collapse/Expand
```tsx
<Button onClick={toggleCollapse} className="h-5 w-5 p-0">
  {collapsed ? (
    <ChevronRight className="h-3.5 w-3.5" />
  ) : (
    <ChevronDown className="h-3.5 w-3.5" />
  )}
</Button>
```

### Copy to Clipboard (Uniwersalne)
```typescript
const handleCopy = async (text: string) => {
  // Try modern clipboard API
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }
  } catch (err) {}

  // Fallback with textarea + execCommand
  try {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    textArea.style.opacity = '0';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
  } catch (fallbackErr) {
    // Final fallback - prompt
    prompt('Skopiuj tekst poniżej (Ctrl+C):', text);
  }
};
```

---

## 10. Komponenty Wiersza

### SectionRow
- Tło: `bg-gray-50`
- Collapse/expand dla sekcji
- Renderuje bezpośrednie pola i tabele

### TableRow
- Tło: domyślne
- Collapse/expand dla tabeli
- Renderuje sekcje tabeli

### TableSectionRow
- Tło: `bg-gray-50`
- Collapse/expand dla sekcji tabeli
- Renderuje pola w sekcji

### FieldRow
- Tło: `bg-white` z `hover:bg-gray-50`
- Pola edytowalne inline
- Ikony typu pola

---

## 11. Dialogi i Modalne

### FieldTypeDialog
**Funkcje:**
- Zmiana typu pola
- Ostrzeżenie o utracie danych
- Wymóg potwierdzenia checkboxem

**Struktura:**
```tsx
<Dialog>
  <DialogContent className="max-w-md">
    <DialogHeader>
      <DialogTitle>Zmiana typu pola</DialogTitle>
      <DialogDescription>...</DialogDescription>
    </DialogHeader>
    
    {/* Select typu */}
    <Select value={selectedType} onValueChange={setSelectedType}>
      {/* Opcje z ikonami */}
    </Select>
    
    {/* Ostrzeżenie */}
    <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
      <div className="flex items-start gap-3">
        <AlertTriangle className="h-5 w-5 text-amber-600" />
        <div className="text-sm">
          <strong>Uwaga!</strong> Zmiana typu pola...
        </div>
      </div>
    </div>
    
    {/* Checkbox potwierdzenia */}
    <div className="flex items-center space-x-2">
      <Checkbox id="confirm" checked={isConfirmed} />
      <label>Zdaję sobie sprawę z ryzyka...</label>
    </div>
    
    {/* Przyciski */}
    <div className="flex justify-end gap-2 pt-4 border-t">
      <Button variant="outline">Anuluj</Button>
      <Button 
        disabled={!isConfirmed}
        className="bg-orange-500 hover:bg-orange-600"
      >
        Zmień typ pola
      </Button>
    </div>
  </DialogContent>
</Dialog>
```

---

## 12. Kontrolki Górne (Controls Row)

### Layout
```tsx
<div className="flex items-center justify-end gap-2">
  {/* Filtry */}
  <Popover>
    <PopoverTrigger asChild>
      <Button variant="ghost" size="sm" className="h-8 w-8 p-0">
        <Filter className={hasActiveFilters() ? 'text-orange-600' : 'text-gray-600'} />
      </Button>
    </PopoverTrigger>
  </Popover>
  
  {/* Kolumny */}
  <Popover>
    <PopoverTrigger asChild>
      <Button variant="ghost" size="sm" className="h-8 w-8 p-0">
        <Columns className="h-4 w-4 text-gray-600" />
      </Button>
    </PopoverTrigger>
  </Popover>
  
  {/* Pełny ekran */}
  <Button variant="ghost" size="sm" className="h-8 w-8 p-0">
    <Maximize className="h-4 w-4 text-gray-600" />
  </Button>
</div>
```

---

## 13. Scrollbar Styling

### Custom Scrollbar (CSS)
```css
* {
  scrollbar-width: thin;
  scrollbar-color: #cbd5e1 #f8fafc;
}

*::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

*::-webkit-scrollbar-track {
  background: #f8fafc;
  border-radius: 4px;
}

*::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 4px;
}

*::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}
```

---

## 14. Responsywność

### Overflow Handling
```tsx
<div className="overflow-x-auto relative">
  <table className="w-full border-collapse">
    {/* Tabela z min-width dla kolumn */}
  </table>
</div>
```

### Sticky Elements
- Pierwsza kolumna (Nazwa systemowa): `sticky left-0`
- Z-index: `z-10` dla sticky columns, `z-20` dla nagłówków
- Shadow dla separacji: `after:shadow-[2px_0_4px_rgba(0,0,0,0.1)]`

---

## 15. Performance i Optymalizacje

### Memoizacja
Rozważ użycie `React.memo` dla:
- FieldRow
- TableRow
- SectionRow
- TableSectionRow

### Callback Stabilizacja
```typescript
const handleUpdateSection = useCallback((index: number, updated: Section) => {
  const updatedSections = [...sections];
  updatedSections[index] = updated;
  onSectionsChange(updatedSections);
}, [sections, onSectionsChange]);
```

### Wirtualizacja (dla dużych list)
Rozważ `react-window` lub `react-virtual` dla >100 wierszy

---

## 16. Accessibility (A11y)

### Keyboard Navigation
- **Tab**: Nawigacja między elementami
- **Enter**: Aktywacja/edycja
- **Escape**: Anulowanie edycji
- **Space**: Toggle checkbox/expand

### ARIA Labels
```tsx
<Button aria-label="Filtruj pola" title="Filtruj pola">
  <Filter />
</Button>

<Checkbox 
  id="filter-type-text"
  aria-labelledby="filter-type-text-label"
/>
<label id="filter-type-text-label">Tekstowe</label>
```

### Focus Management
```typescript
React.useEffect(() => {
  if (isEditing && inputRef.current) {
    inputRef.current.focus();
    inputRef.current.select();
  }
}, [isEditing]);
```

---

## 17. Typy TypeScript

### Podstawowe Typy
```typescript
type FieldType = 'data' | 'data-czas' | 'tekstowe' | 'długi-tekst' 
               | 'kwota' | 'odnośnik' | 'słownik' | 'lista';

interface Field {
  id: string;
  name: string;
  technicalName?: string;
  displayName?: string;
  displayNameEn?: string;
  displayNameDe?: string;
  columnName?: string;
  defaultValue?: string;
  tooltip?: string;
  tooltipEn?: string;
  tooltipDe?: string;
  fieldType?: FieldType;
}

interface TableSection {
  id: string;
  name: string;
  displayName?: string;
  displayNameEn?: string;
  displayNameDe?: string;
  fields: Field[];
  collapsed: boolean;
}

interface Table {
  id: string;
  name: string;
  displayName?: string;
  displayNameEn?: string;
  displayNameDe?: string;
  fields: Field[];
  sections: TableSection[];
  collapsed: boolean;
}

interface Section {
  id: string;
  name: string;
  displayName?: string;
  displayNameEn?: string;
  displayNameDe?: string;
  tooltip?: string;
  tooltipEn?: string;
  tooltipDe?: string;
  fields: Field[];
  tables: Table[];
  collapsed: boolean;
}
```

---

## 18. Best Practices

### 1. State Management
- Pojedyncze źródło prawdy (sections array)
- Immutable updates (spread operator)
- Controlled components

### 2. Component Composition
- Małe, reużywalne komponenty
- Props drilling minimalizacja (consider Context dla głębokiej hierarchii)
- Separation of concerns (UI vs logika)

### 3. Styling
- Tailwind utility-first
- Consistent spacing (multiples of 4px)
- Semantic class names dla custom CSS

### 4. Error Handling
- Graceful degradation (clipboard fallbacks)
- User feedback (toast notifications)
- Validation przed zapisem

### 5. Testing
- Unit tests dla helper functions
- Integration tests dla komponentów
- E2E tests dla krytycznych flow

---

## 19. Wzorce UI

### Empty States
```tsx
{items.length === 0 && (
  <div className="text-center p-8">
    <Icon className="h-8 w-8 text-gray-400 mx-auto mb-3" />
    <h3 className="text-sm font-medium mb-1">Tytuł</h3>
    <p className="text-sm text-gray-500">Opis sytuacji</p>
  </div>
)}
```

### Loading States
```tsx
{isLoading ? (
  <div className="flex items-center justify-center p-8">
    <Loader className="h-6 w-6 animate-spin text-orange-500" />
  </div>
) : (
  /* Content */
)}
```

### Error States
```tsx
{error && (
  <div className="bg-red-50 border border-red-200 rounded-lg p-4">
    <div className="flex items-start gap-3">
      <AlertCircle className="h-5 w-5 text-red-600" />
      <div>
        <h4 className="text-sm font-medium text-red-800">Błąd</h4>
        <p className="text-sm text-red-700">{error.message}</p>
      </div>
    </div>
  </div>
)}
```

---

## 20. Przyszłe Rozszerzenia

### Planowane Funkcjonalności
1. **Sortowanie kolumn** - kliknięcie w nagłówek
2. **Wyszukiwanie** - globalne i per-kolumna
3. **Bulk edit** - edycja wielu pól naraz
4. **Import/Export** - CSV, Excel
5. **Historia zmian** - versioning i undo
6. **Templates** - zapisywanie konfiguracji
7. **Drag & Drop** - reordering pól/sekcji
8. **Walidacja** - custom rules per field type

### Rozważane Biblioteki
- `react-table` / `@tanstack/react-table` - zaawansowane funkcje tabelaryczne
- `react-dnd` - drag and drop
- `react-hook-form` - formularze z walidacją
- `zod` - schema validation
- `zustand` / `jotai` - state management

---

## 21. Migracja z Innych Widoków

### Współdzielone Komponenty
- Button, Input, Select - z `/components/ui`
- Icons - lucide-react
- Dialog, Popover, Tooltip - Radix UI wrappers

### Style Consistency
- Zachowaj branding AMODIT (pomarańczowy)
- Używaj tych samych rozmiarów (14px font)
- Zachowaj spacing system (4px grid)

### Data Flow
- Props drilling vs Context
- Callbacks dla updates
- Optimistic UI updates

---

## Podsumowanie

Dokument ten zawiera wszystkie kluczowe wzorce, style i logikę biznesową z widoku "Lista Pól". Przy tworzeniu nowego projektu:

1. Skopiuj strukturę typów z sekcji 17
2. Zastosuj kolory i branding z sekcji 1
3. Użyj układu tabeli z sekcji 3
4. Zaimplementuj filtry według sekcji 6
5. Dodaj system tłumaczeń z sekcji 8
6. Zastosuj wzorce inline editing z sekcji 5
7. Zachowaj accessibility z sekcji 16

**Kluczowe zasady:**
- Wszystko 14px font size
- Pomarańczowy jako primary color
- Hierarchia przez wcięcia (20px per level)
- Dziedziczenie wartości w tłumaczeniach
- Sticky column z cieniem
- Inline editing z keyboard shortcuts
- Uniwersalny clipboard z fallbackami

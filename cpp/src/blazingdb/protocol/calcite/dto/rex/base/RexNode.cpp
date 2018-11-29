#include "rex/base/RexNode.h"

namespace blazingdb {
namespace protocol {
namespace dto {

RexNode::RexNode()
{ }

RexNode::RexNode(KindName kind, TypeName type)
 : kindName{kind}, typeName{type}
{ }

KindName RexNode::getKindName() {
    return kindName;
}

void RexNode::setKindName(KindName value) {
    kindName = value;
}

TypeName RexNode::getTypeName() {
    return typeName;
}

void RexNode::setTypeName(TypeName value) {
    typeName = value;
}

}  // namespace dto
}  // namespace protocol
}  // namespace blazingdb
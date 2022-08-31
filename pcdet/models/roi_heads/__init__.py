from .roi_head_template import RoIHeadTemplate

from .ted_head import TEDMHead, TEDSHead

__all__ = {
    'RoIHeadTemplate': RoIHeadTemplate,
    'TED2SHead': TEDSHead,
    'TED2MHead': TEDMHead
}
